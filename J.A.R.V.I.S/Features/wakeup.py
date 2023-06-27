from vosk import Model, KaldiRecognizer
from Jarvis import MainExe
import pyaudio
import os
from time import sleep

model = Model("D:\\Bhardwaj\\J.A.R.V.I.S\\Body\\vosk-model-small-en-us-0.15")
recognizer = KaldiRecognizer(model, 16000)

mic = pyaudio.PyAudio()
stream = mic.open(format = pyaudio.paInt16, channels = 1, rate = 16000, input = True, frames_per_buffer = 8192)
stream.start_stream()


def Listen():
    print("")
    print("Listening...")
    print("")

    while True:

        data = stream.read(9000)

        if recognizer.AcceptWaveform(data):
            query = recognizer.Result()
            p = query[14:-3]
            print(f"You : {p}")

            if len(p)>0:
                return p
            
            else:
                break

while True:
    query = Listen()

    if query is not None and "wake up" in query:
        print(">>Starting J.A.R.V.I.S.>>")
        os.startfile("D:\\Bhardwaj\\J.A.R.V.I.S\\Features\\ACDC Highway to Hell.mp3")
        sleep(2)
        os.startfile("D:\\Bhardwaj\\J.A.R.V.I.S\\Jarvis.py")

    else:
        print("Not detected")
