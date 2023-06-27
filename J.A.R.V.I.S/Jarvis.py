from Body.Speak import Speak
from Body.Listen import Listen
from Brain.AIBrain import ReplyBrain
from Brain.Qna import QuestionAnswer
from Arms.iss import international_space_station
from Automations.Whatsapp import OpenWhatsapp
from Automations.Whatsapp import SendWhatsappMessage
import os
from datetime import datetime
import random
import urllib.request
import sys
import json
import requests
import time

def set_reminder(reminder, reminder_time):
    current_time = datetime.datetime.now()
    target_time = datetime.datetime.strptime(reminder_time, "%Y-%m-%d %H:%M")

    # Calculate the time difference in seconds
    time_diff = (target_time - current_time).total_seconds()

    if time_diff <= 0:
        print("Please provide a future time for the reminder.")
    else:
        time.sleep(time_diff)
        print("Reminder:", reminder)
                
def Weather():
    api_key = '536eddd2428449c8a3f132652232506'
    city = 'New Delhi'
    country = 'India'

    # Make the API request
    url = f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={city},{country}'
    response = requests.get(url)
    data = response.json()

    # Extract and print the weather information
    location = data['location']['name']
    current_temp = data['current']['temp_c']
    condition = data['current']['condition']['text']

    Speak(f"Weather in {location} is {current_temp} degrees with {condition}")

def WishMe():
    current_time = datetime.now().time()

    # Format the current time as a string representing the hour
    hour = current_time.strftime("%H")
    time = current_time.strftime("%H:%M")

    greet = ['How may I help you today ?', 'I have indeed been uploaded, sir. We\'re online and ready.', 'How are you today ?', 'I assume that you woke me up ?','Welcome home sir...', 'sir, Good to hear you', 'sir feel free to have a cup of coffee until I set up everything for you, importing prefrences from home interace, reading logs, calculating external and internal data, checking the microphone, initializing audio input and output functionality, all set sir, how may I hep you ?', 'All set sir...', 'Is there anything I can help you with today ?', 'How is your day today ?', 'I am online now', 'I am booted up now, how may I help you today ?']
    greetMe = random.choice(greet)

    if int(hour) >= 6 and int(hour) <=11:
        Speak("Good Morning !")
        Speak("It's " + time)
        Weather()
        Speak(greetMe)

    elif int(hour) >= 12 and int(hour) <= 16:
        Speak("Good Afternoon !")
        Speak("It's " + time)
        Weather()
        Speak(greetMe)

    elif int(hour) >= 17 and int(hour) <= 19:
        Speak("Good Evening !")
        Speak("It's " + time)
        Weather()
        Speak(greetMe)

    else:
        Speak("Well sir, it's too late for you to work now, I would recommend you to take some rest...")
        Speak("It's "  + time)

def MainExecution():   
    while True:
        query = str(Listen())
        
        if query is not None:

            if "hello" in query:
                Speak("Hello Sir! How are you today?")

            elif "weather" in query:
                Weather()

            elif "whatsapp" in query:
                OpenWhatsapp()
                Speak("Opening WhatsApp...")

            elif "message" in query:
                SendWhatsappMessage()

            elif "time" in query:
                hour = datetime.now().strftime("%H")
                minutes = datetime.now().strftime("%M")
                seconds = datetime.now().strftime("%S")
                Speak(f"It's {hour} hours, {minutes} minutes, {seconds} seconds...")

            elif "remember" in query:
                Speak("What should I remember ?")
                reminder_text = Listen()
                Speak("When should i remind it to you ?")
                reminder_datetime = input("Example: 2023-06-26 16:30")
                set_reminder(reminder_text, reminder_datetime)
                Speak("Your reminder has been set Sir")

            elif "bye" in query:
                Speak("Goodbye sir!")
                break

            elif "mute" in query or "exit" in query:
                Speak("Goodbye sir!")
                os.startfile("D:\\Bhardwaj\\J.A.R.V.I.S\\Features\\clap_detection.py")
                os.startfile("D:\\Bhardwaj\\J.A.R.V.I.S\\Features\\wakeup.py")
                break

            elif "who is" in query or "who were" in query or "what is" in query or "what were" in query or "where is" in query or "where was"in query or "answer" in query:
                Reply = QuestionAnswer(query)
                Speak(Reply)

            elif "where is international space station" in query or "where is iss"in query:
                international_space_station()

            elif "file" in query:
                Speak("Should I save it in your private directory sir ?")

                if 'yes' in query:
                    # Specify the directory path
                    directory = '/path/to/directory'

                    # Create the directory if it doesn't exist
                    os.makedirs(directory, exist_ok=True)
                    Speak("What should I name it ?")
                    fileName = Listen()

                    # Specify the file path within the directory
                    filename = os.path.join(directory, f'{fileName}.txt')

                    Speak(f"'{filename}' was created successfully.")

                if 'no' in query:
                    # Specify the directory path
                    directory = '/path/to/directory'

                    # Create the directory if it doesn't exist
                    os.makedirs(directory, exist_ok=True)
                    Speak("What should I name it ?")
                    fileName = Listen()

                    # Specify the file path within the directory
                    filename = os.path.join(directory, f'{fileName}.txt')

                    Speak(f"'{filename}' was created successfully.")

                else:
                    Speak("Sir, can you please clarify ?")
            
            elif "mouse" in query:
                from Automations.VirtuaMouse import VirtualMouse
                VirtualMouse()

            elif "message" in query:
                from Automations.Whatsapp import Whatsapp
                Whatsapp()

            else:
                Reply = ReplyBrain(query)
                Speak(Reply)

if __name__ == '__main__':
    WishMe()
    MainExecution()