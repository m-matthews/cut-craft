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

import pytest
import cutcraft.core as cc
import cutcraft.supports as cs

def test_pier():
    p = cs.Pier(10.0, 2.0, 1.0, [(0.0, 0.0), (4.9, 0.0), (9.8, 0.0)], 0.2)

    # Check equality test.
    assert(p.thickness == 0.2)

    # Check one complete trace.
    assert(len(p.traces) == 1)

    # Check vertical detection.
    assert(p.vertical == True)

    # Check trace is as expected for the specifications provided.
    expected = cc.Trace([0.0,  0.0,  1.0, 1.0, 2.0, 2.0, 1.0, 1.0, 2.0, 2.0, 1.0, 1.0, 0.0],
                        [0.0, 10.0, 10.0, 9.8, 9.8, 5.1, 5.1, 4.9, 4.9, 0.2, 0.2, 0.0, 0.0])
    assert(p.traces[0] == expected)

    # Check supports too close.
    with pytest.raises(Exception):
        p = cs.Pier(10.0, 2.0, 1.0, [(0.0, 0.0), (0.3, 0.0), (9.8, 0.0)], 0.2)