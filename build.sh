#!/bin/bash

set -ETeu -o pipefail


function build_dist() {
  python setup.py bdist_wheel
}

function upload_to_dbfs() {
  local BUILDER="$(whoami)"
  for entry in ./dist/*
  do
    WHL="$entry"
    WHL=${WHL#*./dist/}
  done
  echo ${WHL}
  ERA_DBFS=dbfs:/${BUILDER}/ERA/dist/${WHL}
  echo ${ERA_DBFS}
  dbfs rm ${ERA_DBFS}
  dbfs cp dist/*.whl ${ERA_DBFS}
  rm -rf dist/ build/
}

build_dist
upload_to_dbfs