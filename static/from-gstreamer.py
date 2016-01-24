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
        multifilesink location=input/gst-{pattern}.png sync=false
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
