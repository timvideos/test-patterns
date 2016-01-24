#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# vim: set ts=4 sw=4 et sts=4 ai:

import sys, gi, signal

gi.require_version('Gst', '1.0')
from gi.repository import Gst, GObject

GObject.threads_init()
Gst.init([])

src = Gst.parse_launch("videotestsrc")

import time
mainloop = GObject.MainLoop()
gcontext = mainloop.get_context()

class WaitTillFinished(object):
    def __init__(self, pipe):
        self.finished = False
    
        self.pipe = pipe
        self.pipe.bus.connect("message::eos", self.on_eos)
        self.pipe.bus.connect("message::error", self.on_error)

    def on_eos(self, bus, message):
        self.finished = True

    def on_error(self, bus, message):
        self.finished = True

    def run(self):
        self.pipe.set_state(Gst.State.PLAYING)
        while not self.finished:
            if gcontext.pending():
                gcontext.iteration()
            else:
                time.sleep(0.1)

i = 0
while True:
    current_pattern = src.get_property("pattern")
    if int(current_pattern) != i:
        break

    print(current_pattern.value_nick)

    pipe = Gst.parse_launch("""
        videotestsrc name=src pattern={pattern} num-buffers=1 !
    	video/x-raw,format=RGB,width={width},height={height},framerate=25/1,pixel-aspect-ratio=1/1 !
        pngenc !
        multifilesink location=input/{pattern}.png sync=false
        """.format(
            pattern=current_pattern.value_nick,
            width=1280,
            height=720,
        ))
    pipe.bus.add_signal_watch()
    finished = False

    WaitTillFinished(pipe).run()

    i += 1
    src.set_property("pattern", i)


#for infile in os.listdir(


#from IPython import embed; embed()

"""
(0): smpte            - SMPTE 100% color bars
(1): snow             - Random (television snow)
(2): black            - 100% Black
(3): white            - 100% White
(4): red              - Red
(5): green            - Green
(6): blue             - Blue
(7): checkers-1       - Checkers 1px
(8): checkers-2       - Checkers 2px
(9): checkers-4       - Checkers 4px
(10): checkers-8       - Checkers 8px
(11): circular         - Circular
(12): blink            - Blink
(13): smpte75          - SMPTE 75% color bars
(14): zone-plate       - Zone plate
(15): gamut            - Gamut checkers
(16): chroma-zone-plate - Chroma zone plate
(17): solid-color      - Solid color
(18): ball             - Moving ball
(19): smpte100         - SMPTE 100% color bars
(20): bar              - Bar
(21): pinwheel         - Pinwheel
(22): spokes           - Spokes
"""
