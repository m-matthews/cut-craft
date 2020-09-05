#! /usr/bin/python

import inkex
import simplestyle
import gettext
from cutcraftshape import CutCraftShape
import cutcraft.platforms as cp
from cutcraft.shapes import Box

class CutCraftBox(CutCraftShape):
    def __init__(self):
        CutCraftShape.__init__(self)

        self.arg_parser.add_argument("--width",
                        type=float,
                        dest="width", default=6.0,
                        help="Box Width")
        self.arg_parser.add_argument("--depth",
                        type=float,
                        dest="depth", default=6.0,
                        help="Box Depth")
        self.arg_parser.add_argument("--height",
                        type=float,
                        dest="height", default=60.0,
                        help="Box height")

    def effect(self):
        CutCraftShape.effect(self)

        width = self.svg.unittouu( str(self.options.width) + self.unit )
        depth = self.svg.unittouu( str(self.options.depth) + self.unit )
        height = self.svg.unittouu( str(self.options.height) + self.unit )

        shape = Box(width, depth, height, self.thickness, self.kerf)

        self.pack(shape)

if __name__ == '__main__':
    e = CutCraftBox()
    e.run()
