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

def isclose(a, b, rel_tol=1e-09, abs_tol=0.0):
    # Required as Inkscape uses old version of Python that does not include math.isclose().
    return abs(a-b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)

def iscloselist(a, b):
    # Functionality of isclose() for lists of values.
    return all([isclose(aval, bval) for aval, bval in zip(a, b)])
