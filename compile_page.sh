#!/bin/sh
set -eux

filename=$(echo $1 | sed "s/.md$/.html/")

cat $repo_directory/templates/header.html > $filename


cat $1 |
$marked_exec |
sed -r -e "s%\[\[(.*?)\]\]%<a href=\"./\\1.html\">\\1</a>%g"|
cat >> $filename 


cat $repo_directory/templates/footer.html >> $filename
