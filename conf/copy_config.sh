#!/bin/sh

HERE="$(dirname $0)"

rsync -a --files-from="$HERE/rsync_files.list" / "$HERE/filesystem"
dpkg --get-selections > "$HERE/dpkg.selections"
pip freeze > "$HERE/pip.freeze"

rm -f "$HERE/python_info"
which python >> "$HERE/python_info"
python -V >> "$HERE/python_info"
