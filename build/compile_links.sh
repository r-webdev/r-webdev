#!/bin/sh
set -eu
#script receives text on stdin and replaces all [[foo]] with <a href="./foo.html">foo</a>

sed -r -e "s%\[\[(.*?)\]\]%<a href=\"./\\1.html\">\\1</a>%g"

