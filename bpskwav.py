import pyaudio
import array
import time
import wave

file = wave.open("bpskwav.wav","wb")


#stream = p.open(format=pyaudio.paUInt8,
#                channels=1,
#                rate=48000,
#                frames_per_buffer=128,
#                output=True)

file.setnchannels(1)
file.setsampwidth(1)
file.setframerate(48000)

mark = array.array('B', [0,0,0,0,255,255,255,255]*255)
space = array.array('B',[255,255,255,255,0,0,0,0]*255)

for i in range(32):
    file.writeframes(mark.tobytes())
    file.writeframes(space.tobytes())

file.close()