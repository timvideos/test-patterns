#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# vim: set ts=4 sw=4 et sts=4 ai:

import sys, gi, signal

gi.require_version('Gst', '1.0')
from gi.repository import Gst, GObject

GObject.threads_init()
Gst.init([])

def on_error(bus, message):
    (error, debug) = message.parse_error()
    print('Error-Details: #%u: %s' % (error.code, debug))
    sys.exit(1)

p = """
    videotestsrc pattern={pattern} !
    video/x-raw,width={width},height={height},pixel-aspect-ratio=1/1 !
    videoconvert !
    xvimagesink double-buffer=1
""".format(
    pattern=sys.argv[1],
    width=1280,
    height=720,
    )
print(p)

pipe = Gst.parse_launch(p)
pipe.bus.add_signal_watch()
pipe.bus.connect("message::error", on_error)
pipe.set_state(Gst.State.PLAYING)

mainloop = GObject.MainLoop()
signal.signal(signal.SIGINT, signal.SIG_DFL)
mainloop.run()
