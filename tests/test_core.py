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
import math
from copy import deepcopy
import cutcraft.core as cc

def test_point():
    pt = cc.Point(1.0, 1.0)

    # Check equality test.
    assert(pt == cc.Point(1.0, 1.0))
    assert(pt != cc.Point(2.0, 2.0))

    # Check point addition.
    assert(pt + cc.Point(1.0, 1.0) == cc.Point(2.0, 2.0))
    pt += cc.Point(1.0, 1.0)
    assert(pt == cc.Point(2.0, 2.0))

    # Check distance between two points.
    assert(cc.Point(0.0, 0.0).distance(cc.Point(1.0, 1.0)) == pytest.approx(math.sqrt(2.0)))

    # Check point subtraction.
    pt = cc.Point(1.0, 1.0)
    assert(pt - cc.Point(2.0, 2.0) == cc.Point(-1.0, -1.0))
    pt -= cc.Point(2.0, 2.0)
    assert(pt == cc.Point(-1.0, -1.0))

    # Check unary minus.
    pt = cc.Point(1.0, 2.0)
    assert(-pt == cc.Point(-1.0, -2.0))

    # Check point representations (for coverage completeness).
    pt = cc.Point(1.0, 1.0)
    assert(str(pt) == "(1.0, 1.0)")
    assert(repr(pt) == "Point(1.0, 1.0)")

def test_line():
    ln = cc.Line(cc.Point(0.0, 0.0), cc.Point(1.0, 1.0))

    # Check equality test.
    assert(ln == cc.Line(cc.Point(0.0, 0.0), cc.Point(1.0, 1.0)))
    assert(ln != cc.Line(cc.Point(1.0, 1.0), cc.Point(0.0, 0.0)))

    # Check line intersection.
    assert(ln.intersection(cc.Line(cc.Point(0.0, 1.0), cc.Point(1.0, 0.0))) == cc.Point(0.5, 0.5))
    assert(ln.intersection(cc.Line(cc.Point(0.0, 1.0), cc.Point(0.0, 1.0))) == None)

    # Check point representations (for coverage completeness).
    assert(str(ln) == "((0.0, 0.0), (1.0, 1.0))")
    assert(repr(ln) == "Line(Point(0.0, 0.0), Point(1.0, 1.0))")

def test_rectangle():
    rect1 = cc.Rectangle(cc.Point(1.0, 1.0), cc.Point(3.0, 5.0))
    rect2 = cc.Rectangle(cc.Point(1.0, 5.0), cc.Point(3.0, 1.0))

    # Check size.
    assert(rect1.size() == (2.0, 4.0))

    # Check area.
    assert(rect1.area() == 8.0)

    # Check equality test.
    assert(rect1 == rect2)

    # Check SVG representation.
    assert(rect1.svg() == "M 1.0 1.0 L 3.0 1.0 L 3.0 5.0 L 1.0 5.0 L 1.0 1.0")

    # Check point representations (for coverage completeness).
    assert(str(rect1) == "((1.0, 1.0), (3.0, 5.0))")
    assert(repr(rect1) == "Rectangle(Point(1.0, 1.0), Point(3.0, 5.0))")

def test_trace():
    tr = cc.Trace(x=[1.0, 2.0, 3.0, 4.0, 5.0], y=[2.0, 3.0, 4.0, 5.0, 6.0])

    # Check length.
    assert(len(tr) == 5)

    # Check SVG representation.
    assert(tr.svg() == "M 1.0 2.0 L 2.0 3.0 L 3.0 4.0 L 4.0 5.0 L 5.0 6.0")

    # Check Bounding Box.
    assert(tr.bbox() == (cc.Point(1.0, 2.0), cc.Point(5.0, 6.0)))

    # Check add (Point).
    tradd = tr + cc.Point(6.0, 7.0)
    assert(tradd.x == [1.0, 2.0, 3.0, 4.0, 5.0, 6.0])
    assert(tradd.y == [2.0, 3.0, 4.0, 5.0, 6.0, 7.0])

    # Check add (Trace).
    tradd = tr + cc.Trace(x=[6.0, 7.0], y=[7.0, 8.0])
    assert(tradd.x == [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0])
    assert(tradd.y == [2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0])

    # Check add (other).
    with pytest.raises(Exception):
        tradd = tr + 6.0

    # Check iadd (Point).
    tr = cc.Trace(x=[1.0, 2.0, 3.0, 4.0, 5.0], y=[2.0, 3.0, 4.0, 5.0, 6.0])
    tr += cc.Point(6.0, 7.0)
    assert(tr.x == [1.0, 2.0, 3.0, 4.0, 5.0, 6.0])
    assert(tr.y == [2.0, 3.0, 4.0, 5.0, 6.0, 7.0])

    # Check iadd (Trace).
    tr = cc.Trace(x=[1.0, 2.0, 3.0, 4.0, 5.0], y=[2.0, 3.0, 4.0, 5.0, 6.0])
    tr += cc.Trace(x=[6.0, 7.0], y=[7.0, 8.0])
    assert(tr.x == [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0])
    assert(tr.y == [2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0])

    # Check add (other).
    with pytest.raises(Exception):
        tr += 6.0

    tr = cc.Trace(x=[1.0, 2.0, 3.0, 4.0, 5.0], y=[2.0, 3.0, 4.0, 5.0, 6.0])

    # Check reversal.
    trrev = reversed(tr)
    assert(trrev.x == [5.0, 4.0, 3.0, 2.0, 1.0])
    assert(trrev.y == [6.0, 5.0, 4.0, 3.0, 2.0])

    # Check slices.
    trslice = tr[1::2]
    assert(trslice.x == [2.0, 4.0])
    assert(trslice.y == [3.0, 5.0])

    # Check delete.
    trdel = deepcopy(tr)
    del trdel[2]
    assert(trdel.x == [1.0, 2.0, 4.0, 5.0])
    assert(trdel.y == [2.0, 3.0, 5.0, 6.0])

    # Check update.
    trupdate = deepcopy(tr)
    trupdate[2] = cc.Point(9.0, 9.0)
    assert(trupdate.x == [1.0, 2.0, 9.0, 4.0, 5.0])
    assert(trupdate.y == [2.0, 3.0, 9.0, 5.0, 6.0])

    # Check update (other).
    with pytest.raises(Exception):
        trupdate[2] = 42.0

    # Check close functionality.
    size = len(tr)
    tr.close()
    assert(len(tr) == size + 1)
    assert(tr.x[0] == tr.x[-1] and tr.y[0] == tr.y[-1])

    # Check point representations (for coverage completeness).
    tr = cc.Trace(x=[1.0, 2.0], y=[2.0, 3.0])
    assert(str(tr) == "(" + str(tr.x) + ", " + str(tr.y) + ")")
    assert(repr(tr) == "Trace(" + str(tr.x) + ", " + str(tr.y) + ")")

def test_part():
    pt = cc.Part()
    tr = cc.Trace(x=[1.0, 2.0], y=[2.0, 3.0])

    pt2 = cc.Part() + tr + cc.Trace(x=[0.0, 1.0], y=[0.0, 1.0])

    assert(len(pt.traces) == 0)
    assert(len(pt2.traces) == 2)

    ptadd = pt + tr
    assert(len(pt.traces) == 0)
    assert(len(ptadd.traces) == 1)
    ptadd = ptadd + pt2
    assert(len(ptadd.traces) == 3)

    pt += tr
    assert(len(pt.traces) == 1)
    pt += pt2
    assert(len(pt.traces) == 3)

    # Check Bounding Box.
    assert(pt2.bbox() == cc.Rectangle(cc.Point(0.0, 0.0), cc.Point(2.0, 3.0)))
    assert(pt2.bbox().size() == (2.0, 3.0))
    assert(pt2.bbox().area() == 6.0)

    # Check Area.
    assert(pt2.area() == 6.0)

    # Check add (other).
    with pytest.raises(Exception):
        pt += 42.0
    with pytest.raises(Exception):
        ptadd = pt + 42.0

    # Check close functionality.
    size = len(pt.traces[0])
    pt.close()
    assert(len(pt.traces[0]) == size + 1)

def test_circle():
    sq = cc.Circle(50.0, 4, 0)

    # Check equality test.
    assert(sq.x == pytest.approx([0.0, 50.0, 0.0, -50.0]))
    assert(sq.y == pytest.approx([50.0, 0.0, -50.0, 0.0]))

    # Check half a hexagon trace is a triangle.
    tr = cc.Circle(50.0, 3, 0)
    hx = cc.Circle(50.0, 6, 0)[::2]
    assert(tr.x == hx.x)
    assert(tr.y == hx.y)

    # Test rotation.
    sq = cc.Circle(math.sqrt(200.0), 4, 0, rotation=math.pi/4)

    assert(sq.x == pytest.approx([10.0, 10.0, -10.0, -10.0]))
    assert(sq.y == pytest.approx([10.0, -10.0, -10.0, 10.0]))

    # Check exception when cuts specified without a depth.
    with pytest.raises(ValueError):
        tr = cc.Circle(50.0, 4, 4, thickness=0.5)

    # Check exception when cuts specified with a zero depth.
    with pytest.raises(ValueError):
        tr = cc.Circle(50.0, 4, 4, cutdepth=0.0, thickness=0.5)

    # Check exception when cuts specified without a thickness.
    with pytest.raises(ValueError):
        tr = cc.Circle(50.0, 4, 4, cutdepth=1.0, thickness=0.0)

def test_kerf():
    # Clockwise square.
    sq = cc.Circle(10.0, 4, 0)
    sq.close()

    assert(sq.x == pytest.approx([0.0, 10.0, 0.0, -10.0, 0.0]))
    assert(sq.y == pytest.approx([10.0, 0.0, -10.0, 0.0, 10.0]))

    # Clockwise kerf expands the size of the cut object.
    sq.applykerf(math.sqrt(50.0))

    assert(sq.x == pytest.approx([0.0, 20.0, 0.0, -20.0, 0.0]))
    assert(sq.y == pytest.approx([20.0, 0.0, -20.0, 0.0, 20.0]))

    # Reverse the trace so next kerf cut is inside/smaller.
    sq = reversed(sq)

    assert(sq.x == pytest.approx([0.0, -20.0, 0.0, 20.0, 0.0]))
    assert(sq.y == pytest.approx([20.0, 0.0, -20.0, 0.0, 20.0]))

    sq.applykerf(math.sqrt(50.0))

    assert(sq.x == pytest.approx([0.0, -10.0, 0.0, 10.0, 0.0]))
    assert(sq.y == pytest.approx([10.0, 0.0, -10.0, 0.0, 10.0]))

    # Test kerf on vertical/horizontal lines.
    sq = cc.Circle(math.sqrt(200.0), 4, 0, rotation=math.pi/4)
    sq.close()

    assert(sq.x == pytest.approx([10.0, 10.0, -10.0, -10.0, 10.0]))
    assert(sq.y == pytest.approx([10.0, -10.0, -10.0, 10.0, 10.0]))

    sq.applykerf(10.0)

    assert(sq.x == pytest.approx([20.0, 20.0, -20.0, -20.0, 20.0]))
    assert(sq.y == pytest.approx([20.0, -20.0, -20.0, 20.0, 20.0]))

def test_fingerjoint():
    for style in ('depth','height'):
        fj = cc.FingerJoint(17.0, 2.0, style)
        assert(fj.fingers == pytest.approx([0.0, 4.0, 7.0, 10.0, 13.0, 17.0]))

    fj = cc.FingerJoint(16.0, 2.0, 'width', thickness=1.0)
    assert(fj.fingers == pytest.approx([1.0, 3.0, 5.0, 7.0, 9.0, 11.0, 13.0, 15.0]))
