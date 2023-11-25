#Debadrita Chattopadhyay
#18 November 2023

import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def greetMe():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        speak('Good Morning!')
    elif hour >= 12 and hour < 18:
        speak('Good Afternoon!')
    else:
        speak('Good Evening!')

    speak('I am your personal Voice Assistant. How may I help you ?')

def listenQuery():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-in')
        print("You said: \n", query)

    except Exception as e:
        print("I couldn't understand what you said. Please say that again.")
        return "None"

    return query


if __name__ == "__main__":
    greetMe()
    
    while True:
        query = listenQuery().lower()
        
        if 'hello' in query:
            speak('Hi! I am your personal Voice Assistant. How may I help you ?')

        elif 'search' in query:
            speak('According to Wikipedia...')
            query = query.replace("wikipedia", "")
            
            try:
                results = wikipedia.summary(query, sentences=3)
                speak(results)
                
            except wikipedia.exceptions.DisambiguationError as e:
                speak('Please be more specific.')
            
        elif 'open google' in query :
            webbrowser.open("https://www.google.com")
            
        elif 'date' in query:
            date=datetime.datetime.now().date()
            speak(f'Today\'s date is {date}')
        
        elif 'time' in query:
            time=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f'The time is {time}')
            
        elif 'stop' in query or 'okay' in query or 'thanks' in query:
            speak('I am happy to help you. Bye! ')
            break
        


