#!/bin/bash

rm -rf ./build/*
rm -rf ./dist/*
rmdir ./build   
rmdir ./dist

echo "Building the package..."

python3.10 setup.py sdist bdist_wheel
twine upload dist/*

echo "Build and upload completed."

sleep 1

python3.10 -m pip install mg-pso-gui --user --upgrade --no-cache-dir

echo "Installation completed."

sleep 1

python3.10 -m pip install mg-pso-gui --user --upgrade --no-cache-dir

sleep 1

python3.10 -m pip install mg-pso-gui --user --upgrade --no-cache-dir

/users/robertcordingly/library/python/3.10/bin/mgpsogui