import pyaudio
import array
import time
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paUInt8,
                channels=2,
                rate=8000,
                frames_per_buffer=128,
                output=True)
mark = array.array('B', [0,255,0,255,255,0,255,0,0,255,0,255,255,0,255,0]*20)
space= array.array('B', [0,255,0,255,0,0,0,0,255,0,255,0,255,255,255,255,0,255,0,255,0,0,0,0,255,0,255,0,255,255,255,255]*10)
while True:
    stream.write(mark.tobytes())
    stream.write(space.tobytes())
stream.close()