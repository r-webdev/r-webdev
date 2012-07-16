#!/bin/sh
set -eu

export repo_directory='./'
export marked_exec=./build/marked/bin/marked

find $repo_directory -name \*.md -print0|
xargs -0 -n1 $repo_directory/build/compile_page.sh

