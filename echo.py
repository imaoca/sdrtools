import pyaudio
import array

CHUNK=256
RATE=8000
p=pyaudio.PyAudio()

# stream=p.open(	format = pyaudio.paInt8,
stream=p.open(format = pyaudio.paInt16,
		channels = 1,
		rate = RATE,
		frames_per_buffer = CHUNK,
		input = True,
		output = True)

while stream.is_active():
	input = stream.read(CHUNK)
	output = stream.write(input)

stream.stop_stream()
stream.close()
p.terminate()