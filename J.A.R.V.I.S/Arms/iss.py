import requests
from Body.Speak import Speak

def get_iss_location():
    url = "http://api.open-notify.org/iss-now.json"
    response = requests.get(url)
    data = response.json()
    
    if response.status_code == 200:
        position = data['iss_position']
        latitude = position['latitude']
        longitude = position['longitude']
        return latitude, longitude
    else:
        return None

def international_space_station():
    location = get_iss_location()

    if location:
        latitude, longitude = location
        Speak("Current ISS Location")
        Speak(f"Latitude: {latitude}")
        Speak(f"Longitude: {longitude}")
    else:
        Speak("Failed to retrieve ISS location.")
