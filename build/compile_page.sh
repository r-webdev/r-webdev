#!/bin/sh
set -eu

filename=$(echo $1 | sed "s/.md$/.html/")
title=$(basename $(echo $1 | sed "s/.md$//"))

cat $repo_directory/templates/header.html > $filename


cat $1 |
$repo_directory/build/compile_links.py $title |
$marked_exec |
cat >> $filename


cat $repo_directory/templates/footer.html >> $filename
