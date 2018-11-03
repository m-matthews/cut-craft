#! /usr/bin/python

import gettext
import inkex
import simplestyle
from math import floor
from cutcraft.core import Point, Rectangle

class CutCraftNode(object):
    def __init__(self, rect):
        self.children = []
        self.rectangle = rect
        self.part = None

    def insert(self, part, shape):
        if len(self.children)>0:
            node = self.children[0].insert(part, shape)
            if node is not None:
                return node
            else:
                return self.children[1].insert(part, shape)

        if self.part is not None:
            return None

        pwidth, pheight = part.bbox().expanded().size()
        nwidth, nheight = self.rectangle.expanded().size()

        if pwidth>nwidth or pheight>nheight:
            # Too small.
            return None
        if pwidth==nwidth and pheight==nheight:
            # This node fits.
            self.part = part
            return self

        nleft, ntop = self.rectangle.expanded().topleft.tup()
        nright, nbottom = self.rectangle.expanded().bottomright.tup()

        if nwidth - pwidth > nheight - pheight:
            r1 = Rectangle(Point(nleft, ntop),
                           Point(nleft+pwidth, nbottom))
            r2 = Rectangle(Point(nleft+pwidth+1.0, ntop),
                           Point(nright, nbottom))
        else:
            r1 = Rectangle(Point(nleft, ntop),
                           Point(nright, ntop+pheight))
            r2 = Rectangle(Point(nleft, ntop+pheight+1.0),
                           Point(nright, nbottom))

        self.children = [CutCraftNode(r1), CutCraftNode(r2)]

        return self.children[0].insert(part, shape)

class CutCraftShape(inkex.Effect):
    def __init__(self):
        inkex.Effect.__init__(self)

        self.OptionParser.add_option("--active-tab",
                        action="store", type="string",
                        dest="tab", default="Options",
                        help="The tab selected when OK was pressed")
        self.OptionParser.add_option("--unit",
                        action="store", type="string",
                        dest="unit", default="mm",
                        help="unit of measure for circular pitch and center diameter")
        self.OptionParser.add_option("--thickness",
                        action="store", type="float",
                        dest="thickness", default=20.0,
                        help="Material Thickness")
        self.OptionParser.add_option("--kerf",
                        action="store", type="float",
                        dest="kerf", default=20.0,
                        help="Laser Cutter Kerf")
        self.OptionParser.add_option("--linethickness",
                        action="store", type="string",
                        dest="linethickness", default="1px",
                        help="Line Thickness")

    def effect(self):
        self.unit = self.options.unit
        self.thickness = self.unittouu( str(self.options.thickness) + self.unit)
        self.kerf = self.unittouu( str(self.options.kerf) + self.unit)
        self.linethickness = self.unittouu(self.options.linethickness)

        svg = self.document.getroot()
        self.docwidth = self.unittouu(svg.get('width'))
        self.docheight = self.unittouu(svg.get('height'))

        self.parent=self.current_layer

        layer = inkex.etree.SubElement(svg, 'g')
        layer.set(inkex.addNS('label', 'inkscape'), 'newlayer')
        layer.set(inkex.addNS('groupmode', 'inkscape'), 'layer')

    def _debug(self, string):
        inkex.debug( gettext.gettext(str(string)) )

    def _error(self, string):
        inkex.errormsg( gettext.gettext(str(string)) )

    def pack(self, shape):
        # Pack the individual parts onto the current canvas.
        line_style = { 'stroke': '#000000',
                       'stroke-width': str(self.linethickness),
                       'fill': 'none' }

        items = sorted([(p[0].area(),p[0]) for p in shape.parts], reverse=True)

        rootnode = CutCraftNode(Rectangle(Point(0.0, 0.0), Point(floor(self.docwidth), floor(self.docheight))))

        for i, (_, part) in enumerate(items):
            node = rootnode.insert(part, self)
            if node is None:
                self._error("ERROR: Cannot fit parts onto canvas.\n" +
                            "Try a larger canvas and then manually arrange if required.")
                exit()

            bbox = part.bbox().expanded()
            part += -bbox.topleft
            part += node.rectangle.topleft

            line_attribs = { 'style' : simplestyle.formatStyle(line_style),
                            inkex.addNS('label','inkscape') : 'Test ' + str(i),
                            'd' : part.svg() }
            _ = inkex.etree.SubElement(self.parent, inkex.addNS('path','svg'), line_attribs)
