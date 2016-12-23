# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 20:42:56 2016

@author: Cannon
"""

#practice

import thinkdsp

signal = thinkdsp.TriangleSignal(440)
#signal.plot()

wave = signal.make_wave(duration=0.01, framerate=10000)
spectrum = wave.make_spectrum()

spectrum.hs[0]
