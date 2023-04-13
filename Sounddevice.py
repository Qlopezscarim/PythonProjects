import sounddevice as sd
import speech_recognition as sr
print(sd.query_devices())
sd.default.dtype='int32', 'int32'
sd.default.device[0] = 2
fs = 44100  # Sample rate
seconds = 9  # Duration of recording

#No longer place anywhere
myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
sd.wait()  # Wait until recording is finished
from scipy.io import wavfile
wavfile.write('words_to_decode.wav', fs, myrecording)
print("done")
r = sr.Recognizer()
with sr.AudioFile("words_to_decode.wav") as source:
    # listen for the data (load audio to memory)
    r.adjust_for_ambient_noise(source)
    audio_data = r.record(source)
    # recognize (convert from speech to text)
    text = r.recognize_google(audio_data, language = 'en-IN', show_all = True )
    print(text)
    print(text.get('alternative')[0].get('transcript'))