#!/bin/bash
# Convert batches of .ui files in static folder primecounter/view/gen/qt to 
# to python source files using pyside-uic.

SCRIPT_PATH="`dirname \"$0\"`"                  # relative
SCRIPT_PATH="`( cd \"$SCRIPT_PATH\" && pwd )`"  # absolutized and normalized
if [ -z "$SCRIPT_PATH" ] ; then
  # SCRIPT_PATH inaccessible. Exit.
  exit 1  # fail
fi
echo "$SCRIPT_PATH"

for file in $SCRIPT_PATH/../primecounter/view/gen/qt/*; do
    filename=${file##*/}
    filename=${filename%.ui}
    echo "Converting $filename.ui to $filename.py..."
    pyside-uic $file -o $SCRIPT_PATH/../primecounter/view/gen/$filename".py"
done

echo "All ui files in  view\gen converted successfully!"
