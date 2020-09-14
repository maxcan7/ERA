#!/bin/bash

set -ETeu -o pipefail


function build_dist() {
  python setup.py bdist_wheel
}


build_dist
