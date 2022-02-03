import wave
import math
import numpy as np

fname='stanag3.wav' 
FQ= 1800.0*np.pi*2.0/44100
wind= 24            # windows
waveFile = wave.open(fname, 'r')
q=[];i=[]
# for j in range(waveFile.getnframes()):
for j in range(4000):    
      d = int.from_bytes(waveFile.readframes(1), byteorder='little')
      q.append(d*np.sin(FQ*j))
      i.append(d*np.cos(FQ*j))
      Qsum =  sum(q)
      Isum =  sum(i)
      print(Qsum,Isum,math.atan2(Qsum,Isum),sep=",")
      if j>wind:
            q.pop(0)
            i.pop(0)
waveFile.close()