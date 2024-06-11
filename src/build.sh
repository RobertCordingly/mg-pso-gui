#!/bin/bash

rm -rf ./build/*
rm -rf ./dist/*
rmdir ./build   
rmdir ./dist

python3.10 setup.py sdist bdist_wheel
twine upload dist/*

sleep 1

python3.10 -m pip install mg-pso-gui --user --upgrade

sleep 1

python3.10 -m pip install mg-pso-gui --user --upgrade

sleep 1

python3.10 -m pip install mg-pso-gui --user --upgrade

/users/robertcordingly/library/python/3.10/bin/mgpsogui