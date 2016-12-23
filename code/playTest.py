import thinkdsp

moduleName = input('thinkdsp')
import_module(moduleName)

thinkdsp.play_wave(filename='/Users/Cannon/Music/SmokeRings.wav', player = 'aplay')
