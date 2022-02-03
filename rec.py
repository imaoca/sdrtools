import pyaudio
import array

CHUNK=1024
RATE=8000
p=pyaudio.PyAudio()

stream=p.open(	format = pyaudio.paInt16,
		channels = 1,
		rate = RATE,
		frames_per_buffer = CHUNK,
		input = True,
		output = True)
input = stream.read(CHUNK)
s0 = array.array('h',input)
for i in s0:
    print (i)

stream.stop_stream()
stream.close()
p.terminate()