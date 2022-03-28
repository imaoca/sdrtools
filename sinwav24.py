import pyaudio
import array
import time
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paUInt8,
                channels=1,
                rate=24000,
                frames_per_buffer=128,
                output=True)
tone = array.array('B', [0,255]*256)
while True:
  time.sleep(1)
  for i in range(0, 64):
    stream.write(tone.tobytes())
stream.close()