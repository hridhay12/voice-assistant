import pyttsx3
import speech_recognition as sr
import datetime
import os
import requests
import time

# --- 1. THE SPEAK FUNCTION ---
def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 170) 
    print(f"Assistant says: {text}")    
    engine.say(text)
    engine.runAndWait()
    engine.stop()

# --- 2. THE LISTENING FUNCTION ---
def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("\n[LISTENING...]")
        r.pause_threshold = 0.8
        r.adjust_for_ambient_noise(source, duration=1)
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=5)
            print("[RECOGNIZING...]")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}")
            return query.lower()
        except Exception:
            return "none"

# --- 3. THE MAIN LOGIC LOOP ---
def run_assistant():
    speak("Assistant is online. How can I help?")

    while True:
        query = take_command()

        # --- PRIORITY 1: EXIT ---
        if 'stop' in query or 'exit' in query or 'goodbye' in query:
            speak("Goodbye! Closing the program.")
            break

        # --- PRIORITY 3:  Date and Time ---
        elif 'time' in query:
            time_now = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The time is {time_now}")
        elif 'date' in query:
            date_now = datetime.datetime.now().strftime("%B %d, %Y")
            speak(f"Today's date is {date_now}")
        # --- PRIORITY 2: GREETINGS ---
        elif 'hello' in query or 'hi' in query or 'Hello' in query or 'Hi' in query:
            speak("Hello! How can I assist you today?")
        elif 'how are you' in query:
            speak("I'm just a program, but thanks for asking! How can I help you?")
            
        # --- PRIORITY 4: WEATHER ---
        elif 'weather' in query:
            speak("Which city?")
            city = take_command().strip()
            if city != "none":
                speak(f"Checking weather for {city}")
                # Using the 'Force' method that worked for you
                url = f"https://www.google.com/search?q=weather+in+{city.replace(' ', '+')}"
                os.system(f"start {url}")

        # --- PRIORITY 5: GENERAL SEARCH (Keep this last!) ---
        elif 'search for' in query or 'google' in query:
            search_query = query.replace("search for", "").replace("google", "").strip()
            if search_query != "none":
                speak(f"Searching for {search_query}")
                url = f"https://www.google.com/search?q={search_query.replace(' ', '+')}"
                os.system(f"start {url}")

        # --- FALLBACK ---
        elif query != "none":
            print(f"I heard '{query}', but I don't have a command for that yet.")

# --- 4. START ---
if __name__ == "__main__":
    # Ensure requests is installed
    try:
        import requests
    except ImportError:
        print("Error: 'requests' library not found. Run: py -m pip install requests")
    
    run_assistant()