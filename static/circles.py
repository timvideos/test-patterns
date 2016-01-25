#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# vim: set ts=4 sw=4 et sts=4 ai:

import numpy as np
import scipy
from scipy import ndimage
from scipy.misc import imsave

h = 720
w = 1280
f = np.zeros((h, w), dtype=np.uint32)

for s in [1, 4, 16, 32, 64]:
    sx, sy = f.shape
    X, Y = np.ogrid[0:sx, 0:sy]

    r = np.hypot(X - sx/2, Y - sy/2)

    n = round(w/2/s)
    rbin = (n * r/r.max()).astype(np.int)
    radial_mean = ndimage.mean(f, labels=rbin, index=np.arange(1, rbin.max() +1))

    imsave('input/circles-{0:02}px.png'.format(s), rbin)
