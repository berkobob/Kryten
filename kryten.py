#!/usr/bin/env python3

import snowboydecoder
import speech_recognition as sr
from gtts import gTTS
import subprocess, os

krytensaid = False;

listening = snowboydecoder.HotwordDetector("resources/Kryten.pmdl",
        sensitivity=0.5, audio_gain=2)

def say(text):
    print (text)
    tts = gTTS(text=text, lang='en')
    tts.save("said.mp3")
    with open(os.devnull, "w") as f:
        subprocess.Popen(["mpg321", "said.mp3"], stderr=f)

say ("Listening")

def krytenSaid():
    global krytensaid
    krytensaid = True;
    snowboydecoder.play_audio_file()

def  interrupt():
   global krytensaid
   return krytensaid

listening.start(detected_callback=krytenSaid, interrupt_check=interrupt)

listening.terminate()

r = sr.Recognizer()
with sr.Microphone(device_index=4, sample_rate=16000,
        chunk_size=1024) as source:
    r.adjust_for_ambient_noise(source, duration=1)
    say ("someone said Kryten")
    audio = r.listen(source)

try:
	said = r.recognize_google(audio)
	say("You said: " + said)
except LookupError:
    print("Could not understand audio")
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))

