#! /usr/bin/python

import inkex
import simplestyle
import gettext
from cutcraftshape import CutCraftShape
import cutcraft.platforms as cp
from cutcraft.shapes import RollerBot

class CutCraftRollerBot(CutCraftShape):
    def __init__(self):
        CutCraftShape.__init__(self)

        self.OptionParser.add_option("--supwidth",
                        action="store", type="float",
                        dest="supwidth", default=6.0,
                        help="Support Width")

    def effect(self):
        CutCraftShape.effect(self)

        supwidth = self.unittouu( str(self.options.supwidth) + self.unit )

        # Constants in the current RollerBot design.
        wheelradius = self.unittouu( str(100.0) + "mm" )
        upperradius = self.unittouu( str(92.0) + "mm" )
        lowerradius = self.unittouu( str(82.0) + "mm" )
        facesize = self.unittouu( str(50.0) + "mm" )
        barsize = self.unittouu( str(25.4) + "mm" )
        scale = self.unittouu( str(1.0) + "mm" )

        primarygapwidth = self.unittouu( str(70.0) + "mm" ) # Must be greater than width of Raspberry PI / Arduino.
        secondarygapwidth = self.unittouu( str(25.0) + "mm" )
        width = primarygapwidth*2.0 + secondarygapwidth*2.0 + self.thickness*5.0

        shape = RollerBot(width, supwidth, wheelradius, upperradius, lowerradius,
                          facesize, barsize, primarygapwidth, secondarygapwidth, scale,
                          self.thickness, self.kerf)

        self.pack(shape)

if __name__ == '__main__':
    e = CutCraftRollerBot()
    e.affect()
