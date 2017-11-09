#!/bin/bash

set -e
export LC_ALL=C.UTF-8
export LANG=C.UTF-8

# cd to parent of script's directory (i.e. project root)
cd "${0%/*}"/..

echo '==== Flake8 ===='

flake8 ./python/

echo
echo
echo

echo '==== Black ====='

black --check --diff ./python/
