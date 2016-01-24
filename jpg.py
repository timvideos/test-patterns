#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# vim: set ts=4 sw=4 et sts=4 ai:

import os
import subprocess

quality_levels = [50, 75, 85, 100]

for f in os.listdir("input"):
    in_file, ext = os.path.splitext(f)
    if ext not in ('.png',):
        continue

    for q in quality_levels:
        jpg_dir = "jpg-q{0:03}".format(q)
        if not os.path.exists(jpg_dir):
            os.mkdir(jpg_dir)

        subprocess.check_call("""
convert \
    input/{in_file}.png \
    -quality {q} \
    {jpg_dir}/{in_file}.jpg \
            """.format(
                q=q,
                in_file=in_file,
                jpg_dir=jpg_dir,
            ),
            shell=True)

        cmp_dir = "jpg-c{0:03}".format(q)
        if not os.path.exists(cmp_dir):
            os.mkdir(cmp_dir)

        subprocess.check_call("""
compare \
    -verbose -metric mae \
    input/{in_file}.png \
    {jpg_dir}/{in_file}.jpg \
    {cmp_dir}/{in_file}.png \
            """.format(
                q=q,
                in_file=in_file,
                jpg_dir=jpg_dir,
                cmp_dir=cmp_dir,
            ),
            shell=True,
            stderr=open(os.path.join(cmp_dir, "{0}.txt".format(in_file)), "w"))

