[![Python Test](https://github.com/m-matthews/cut-craft/actions/workflows/push-pytest.yml/badge.svg)](https://github.com/m-matthews/cut-craft/actions/workflows/push-pytest.yml)

# cut-craft


## Overview

**cut-craft** is a Python application for creating model templates which can be manufactured with laser cutting techniques.

This repository contains a Python module to create paths suitable for laser cutting.

The current version includes [Inkscape](https://inkscape.org) integration.  Future versions will include a plugin for [Blender](https://www.blender.org) and/or [FreeCAD](https://www.freecadweb.org/) to be able to render the assembled shapes in 3D.


## Why Another BoxMaker?

There are many Inkscape Tabbed BoxMakers already (eg: [Boxes.py](https://github.com/florianfesti/boxes), [TabbedBoxMaker](https://github.com/paulh-rnd/TabbedBoxMaker), [InkScapeBoxMaker](https://github.com/Wallenstein61/InkScapeBoxMaker) etc), and these should be examined to see if they meet your requirements.

The **cut-craft** implementation has been created to:

1) Define unique objects that are not available or suitable for generic libraries.
2) Include the ability to create 3D renders of the assembled products in [Blender](https://www.blender.org) and/or [FreeCAD](https://www.freecadweb.org/).


## Installation

The current **Inkscape** installation can be performed by following the instructions in the [inkscape](inkscape/README.md) folder.
