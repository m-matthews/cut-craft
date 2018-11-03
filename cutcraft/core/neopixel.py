# -*- coding: utf-8 -*-
# Copyright (C) 2018 Michael Matthews
#
#   This file is part of CutCraft.
#
#   CutCraft is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   CutCraft is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with CutCraft.  If not, see <http://www.gnu.org/licenses/>.

from .point import Point
from .trace import Trace
from .part import Part
from math import pi, sin, cos

class NeoPixel(Part):
    rings = [[1, 0 / 100], [6, 16/2 / 100], [12, 30/2 / 100]]
    size = 2.5 / 100

    """ Line class defined by start and end Points. """
    def __init__(self, origin=Point(0.0, 0.0), thickness=0.0, kerf=0.0):
        super(NeoPixel, self).__init__()
        self.thickness = thickness
        self.kerf = kerf

        for ring in self.rings:
            pixels = ring[0]
            radius = ring[1]
            for pixel in range(pixels):
                seg = Trace()
                a = pi*2 * pixel / pixels
                self._pixel(seg, origin + Point(sin(a) * radius, cos(a) * radius), pi/4 + a)
                self += seg
        return

    def _pixel(self, seg, position, rotation):
        x = []
        y = []
        xo = position.x
        yo = position.y
        for corner in range(4):
            # Points added in counterclockwise direction as this is an inner cut.
            a = rotation-corner/4*2*pi
            x.append(xo + sin(a) * self.size)
            y.append(yo + cos(a) * self.size)
        seg.x += x
        seg.y += y
        return
