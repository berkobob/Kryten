#!/usr/bin/env python3

import snowboydecoder
import speech_recognition as sr
import subprocess, os, random
from gtts import gTTS

import follow

greetings = []
running = True

def say(text):
    print (text)
    tts = gTTS(text=text, lang='en')
    tts.save("said.mp3")
    with open(os.devnull, "w") as f:
        subprocess.call(["mpg321", "said.mp3"], stderr=f)

def krytenSaid():
    global krytensaid
    krytensaid = True;
    snowboydecoder.play_audio_file(snowboydecoder.DETECT_DING)

try:
    f = open("resources/greetings",'r')
    for line in f:
        greetings.append(line.rstrip())
    f.close()
except:
    greetings.append("At your command")

while(running):
    krytensaid = False
    snowboydecoder.play_audio_file(snowboydecoder.DETECT_DING)

    listening = snowboydecoder.HotwordDetector("resources/Kryten.pmdl",
            sensitivity=0.5, audio_gain=2)

    listening.start(detected_callback=krytenSaid,
            interrupt_check=lambda:krytensaid)

    listening.terminate()

    r = sr.Recognizer()
    with sr.Microphone(device_index=4, sample_rate=16000,
            chunk_size=1024) as source:
        r.adjust_for_ambient_noise(source, duration=1)
        say (greetings[random.randint(0,len(greetings)-1)])
        audio = r.listen(source)

    try:
        said = r.recognize_google(audio)
        say("You said: " + said)
        if ("stop" in said):
            running = False
        if ("follow" in said):
            say("OK. I'm going to try and start the follow me program")
            follow.me()
    except LookupError:
        say("Could not understand audio")
    except sr.UnknownValueError:
        say("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        say("Could not request results from Google Speech Recognition service; {0}".format(e))

