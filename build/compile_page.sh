#!/bin/sh
set -eux

filename=$(echo $1 | sed "s/.md$/.html/")

cat $repo_directory/templates/header.html > $filename


cat $1 |
$marked_exec |
$repo_directory/build/compile_links.py |
cat >> $filename


cat $repo_directory/templates/footer.html >> $filename
