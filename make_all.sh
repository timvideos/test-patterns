#!/bin/bash -ex

sudo apt-get install python3-scipy python3-pil gstreamer1.0-plugins-*

cd static

python3 circles.py
python3 edges.py
python3 lines.py
python3 from-gstreamer.py

python3 jpg.py
