import pyaudio
import array
import time
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paUInt8,
                channels=1,
                rate=48000,
                frames_per_buffer=128,
                output=True)
mark = array.array('B', [0,255]*255)
while True:
    stream.write(mark.tobytes())
stream.close()