#!/bin/sh
set -eux
git submodule init
git submodule update
cd build/marked
make

