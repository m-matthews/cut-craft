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

import cutcraft.shapes as cs

def test_shape():
    sh = cs.Shape(1.0, 0.1)

    # Check equality test.
    assert(sh.thickness == 1.0)
    assert(sh.kerf == 0.1)

    cyl = cs.Cylinder(30.0, 10.0, 6.0, 4, 4, 2.0, 4.0, 3, thickness=1.0, kerf=0.1)
    assert(len(cyl.parts) == 7)
