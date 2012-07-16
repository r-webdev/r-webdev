#!/bin/sh
set -eu

export repo_directory=$HOME/r-webdev
export marked_exec=$HOME/r-webdev/build/marked/bin/marked

find $repo_directory -name \*.md -print0|
xargs -0 -n1 $repo_directory/build/compile_page.sh

