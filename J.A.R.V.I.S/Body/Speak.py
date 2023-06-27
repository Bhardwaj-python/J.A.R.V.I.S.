import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 175)

def Speak(audio):
    print("")
    print("J.A.R.V.I.S. : " + audio)
    print("")
    engine.say(audio)
    engine.runAndWait()
