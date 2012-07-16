#!/bin/sh
set -eux

export repo_directory=$HOME/r-webdev
export marked_exec=$HOME/marked/bin/marked

find $repo_directory -name \*.md -print0|
xargs -0 -n1 $repo_directory/compile_page.sh

