from Body.Listen import Listen
from Body.Speak import Speak
import webbrowser
import pywhatkit
from datetime import datetime

def OpenWhatsapp():
    webbrowser.open("https://web.whatsapp.com/")

def SendWhatsappMessage():
    Speak("What is the message ?")
    msg = Listen()
    Speak("to whom should I send the message, to your dad, your mom oranyone else ?")

    dad = "your_number_here"
    mom = "your_number_here"

    while True:
        query = Listen()
        if "dad" in query:
            pywhatkit.sendwhatmsg(dad, msg, int(input("Hours: ")), int(input("Minutes: ")))
            Speak("Your message has been sent")
        
        elif "mom" in query or "mum" in query:
            pywhatkit.sendwhatmsg(mom, msg, int(input("Hours: ")), int(input("Minutes: ")))
            Speak("Your message has been sent")

        elif "aunt" in query or "ant" in query:
            pywhatkit.sendwhatmsg(aunt, msg, int(input("Hours: ")), int(input("Minutes: ")))
            Speak("Your message has been sent")

        elif "dishant" in query:
            pywhatkit.sendwhatmsg(dishant, msg, int(input("Hours: ")), int(input("Minutes: ")))
            Speak("Your message has been sent")

        elif "abin" in query:
            pywhatkit.sendwhatmsg(abin, msg, int(input("Hours: ")), int(input("Minutes: ")))
            Speak("Your message has been sent")

        elif "cancel" in query:
            break
    
        elif "other" in query or "else" in query:
            Speak("What is the number ?")
            number = input("Enter the number with country code: ")
            pywhatkit.sendwhatmsg(number, msg, int(input("Hours: ")), int(input("Minutes: ")))
            Speak("Your message has been sent")

        else:
            Speak("Sir please, I need your clarification...")

