#!/usr/bin/env bash

DEST=~/.config/inkscape/extensions
echo "Updating Inkscape local extensions in folder '$DEST'."

echo "Removing existing cut-craft extensions."
#rm $DEST/cutcraft*
rm -rf $DEST/cutcraft*

echo "Installating latest cut-craft extensions."
cp cutcraft*.py $DEST
cp cutcraft*.inx $DEST
mkdir  $DEST/cutcraft
cd ../cutcraft
cp --parents `find . -name \*.py` $DEST/cutcraft


echo "Installation of cut-craft extensions for Inkscape complete."
echo "Restart Inkscape to ensure updates are available."
