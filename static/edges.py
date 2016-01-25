#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# vim: set ts=4 sw=4 et sts=4 ai:

import numpy as np
from scipy.misc import imsave

h = 720
w = 1280

white = [0xff, 0xff, 0xff]
black = [0, 0, 0]

sizes=[1,2,4,8,16,32,64,128,256]

for s in sizes:
    data = np.zeros((h, w, 3), dtype=np.uint8)

    # Left
    data[0:h, 0:s] = white
    # Right
    data[0:h, w-s:w] = white

    # Top
    data[0:s, 0:w] = white
    # Bottom
    data[h-s:h, 0:w] = white

    imsave('input/edges-{0:03}px.png'.format(s), data)

