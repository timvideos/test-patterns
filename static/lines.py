#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# vim: set ts=4 sw=4 et sts=4 ai:

import numpy as np
from scipy.misc import imsave


h = 720
w = 1280

white = ('w', [0xff, 0xff, 0xff])
black = ('b', [0, 0, 0])
red = ('r', [0xff, 0, 0])
blue = ('b', [0, 0, 0xff])
green = ('g', [0, 0xff, 0])

sizes=[1,2,4,8,16,32,64,128,256]

for (c1n, c1v), (c2n, c2v) in [(black, white), (red, green), (blue, red)]:
    for s in sizes:
        # Vertical
        data = np.zeros((h, w, 3), dtype=np.uint8)
        data[0:h, 0:w] = c1v
        for i in range(0, w, s*2):
            data[0:h, i:i+s] = c2v
        imsave('input/lines-{1}{2}-v-{0:03}px.png'.format(s, c1n, c2n), data)

        # Horizontal
        data = np.zeros((h, w, 3), dtype=np.uint8)
        data[0:h, 0:w] = c1v
        for i in range(0, h, s*2):
            data[i:i+s, 0:w] = c2v
        imsave('input/lines-{1}{2}-h-{0:03}px.png'.format(s, c1n, c2n), data)
