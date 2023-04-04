from playsound import playsound
from gtts import gTTs

def playaudio(audio):
    playsound(audio)

def my_audio(text):
    audio=gTTS(text)
    audio.save(audio_test file.mp3)
    playaudio(audio_test file.mp3)

audio_test("Maine tumhare liye samose banaye haii..")