#! /usr/bin/python

import inkex
import simplestyle
import gettext
from cutcraftshape import CutCraftShape
import cutcraft.platforms as cp
from cutcraft.shapes import Cylinder

class CutCraftCylinder(CutCraftShape):
    def __init__(self):
        CutCraftShape.__init__(self)

        self.OptionParser.add_option("--vertices",
                        action="store", type="int",
                        dest="vertices", default=3,
                        help="Number of vertices")
        self.OptionParser.add_option("--levels",
                        action="store", type="int",
                        dest="levels", default=3,
                        help="Number of levels")
        self.OptionParser.add_option("--supports",
                        action="store", type="int",
                        dest="supports", default=3,
                        help="Number of supports")
        self.OptionParser.add_option("--height",
                        action="store", type="float",
                        dest="height", default=60.0,
                        help="Cylinder height")
        self.OptionParser.add_option("--outer",
                        action="store", type="float",
                        dest="outer", default=60.0,
                        help="Diameter of cylinder")
        self.OptionParser.add_option("--inner",
                        action="store", type="float",
                        dest="inner", default=30.0,
                        help="Diameter of central hole - 0.0 for no hole")

    def effect(self):
        CutCraftShape.effect(self)

        vertices = self.options.vertices
        levels = self.options.levels
        supports = self.options.supports
        height = self.unittouu( str(self.options.height) + self.unit )
        outer = self.unittouu( str(self.options.outer) + self.unit )
        inner = self.unittouu( str(self.options.inner) + self.unit )

        if outer<=inner:
            self._error("ERROR: Outer diameter must be greater than inner diameter.")
            exit()

        shape = Cylinder(height, outer, inner, vertices, supports, 2.0*self.thickness, levels,
                         self.thickness, self.kerf)

        self.pack(shape)

if __name__ == '__main__':
    e = CutCraftCylinder()
    e.affect()
