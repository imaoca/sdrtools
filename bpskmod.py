import pyaudio
import array
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paUInt8,
                channels=1,
                rate=8000,
                frames_per_buffer=128,
                output=True)

s0 = array.array('B', [0,0,0,0,0xff,0xff,0xff,0xff]*10)
s1 = array.array('B', [0xff,0xff,0xff,0xff,0,0,0,0]*10)
dt = [1,0,0,1,0,0,1,0,1,0]*16

for i in dt:
    if i==0 :
        stream.write(s0.tobytes()) 
    else:
        stream.write(s1.tobytes()) 
stream.close()