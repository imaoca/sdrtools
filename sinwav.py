import pyaudio
#import numpy as np
import array
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paUInt8,
                channels=1,
                rate=8000,
                frames_per_buffer=128,
                output=True)
#samples = np.sin(np.arange(512))
samples = array.array('B', [0,255]*256)
for i in range(0, 8):
    stream.write(samples.tobytes())
stream.close()