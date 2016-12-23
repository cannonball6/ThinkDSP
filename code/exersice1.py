# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


from __future__ import print_function, division

import thinkdsp
import thinkplot

import warnings
warnings.filterwarnings('ignore')



#thinkdsp.play_wave(filename='/Users/Cannon/Music/SmokeRings.wav', player = 'aplay')

cos_sig = thinkdsp.CosSignal(freq=440, amp=1.0, offset=0)
sin_sig = thinkdsp.SinSignal(freq=880, amp=0.5, offset=0)

#cos_sig.plot()
#thinkplot.config(xlabel='Time (s)')
#sin_sig.plot()

mix = sin_sig + cos_sig

wave = mix.make_wave(duration=0.5, start=0, framerate=11025)

#wave.play('temp.wav')


period = mix.period
segment = wave.segment(start=0, duration=period*3)



start = 1.2
duration = 0.6
segment = wave.segment(start, duration)


spectrum = wave.make_spectrum()

spectrum.plot()
thinkplot.config(xlabel='Freq (Hz)')