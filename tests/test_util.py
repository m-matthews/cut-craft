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

import cutcraft.util as cu

def test_util():
    # Check isclose().
    assert(cu.isclose(1.0, 1.0) == True)
    assert(cu.isclose(1.0, 2.0) == False)
    assert(cu.isclose(1.0 + 1e-10, 1.0) == True)
    assert(cu.isclose(1.0 + 1e-8, 1.0) == False)
