import ntpath
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import cv2
from requests import get
import pywhatkit as kit


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voices', voices[0].id)


def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour <= 10:
        speak("Good Morning Sir,")

    elif hour > 10 and hour <= 17:
        speak("Good Afternoon Sir,")

    elif hour > 17 and hour <= 20:
        speak("Good Evening Sir,")

    else:
        speak("It is night time sir. ")
    speak("I am Jarvis, your virtual assistant. Tell me how should i proceed.")


def takecommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=2, phrase_time_limit=5)

    try:
        print("Recognizing...")
        # Using google for voice recognition.
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")  # User query will be printed.

    except Exception as e:
        # print(e)
        # Say that again will be printed in case of improper voice
        speak("Say that again please...")
        return "None"  # None string will be returned
    return query


if __name__ == '__main__':
    
    wishme()
    while True:
        query = takecommand().lower()

        if 'wikipedia' in query:
            speak("Searching Wikipedia")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak('According to wikipedia')
            print(results)
            speak(results)

        elif 'youtube' in query:
            webbrowser.open('https://www.youtube.com/')

        elif 'coding ninjas' in query:
            webbrowser.open(
                'https://classroom.codingninjas.com/app/classroom/batch/6206/contents/topics')

        elif 'linked in' in query:
            webbrowser.open('https://www.linkedin.com/feed/')

        elif 'git hub' in query:
            webbrowser.open('https://github.com/nimizh')

        elif 'facebook' in query:
            webbrowser.open('https://www.facebook.com/')

        elif 'instagram' in query:
            webbrowser.open('https://www.instagram.com/')

        elif 'play music' in query:
            music_directory = 'D:\\Music'
            songs = os.listdir(music_directory)
            print(songs)
            os.startfile(os.path.join(music_directory, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime('%H:%M:%S')
            speak(f'Sir, the time is {strTime}')

        elif 'open code' in query:
            codePath = '"D:\\Microsoft VS Code\\Code.exe"'
            os.startfile(codePath)

        elif 'open notepad' in query:
            npath = 'C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories'
            os.startfile(ntpath)

        elif 'command prompt' in query:
            os.system('start cmd')

        elif 'open camera' in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k == 27:
                    break
                cap.release()
                cv2.destroyAllWindows()

        elif 'ip address' in query:
            ip = get('http://api.ipify.org/')
            speak(f'Your IP Address is {ip}')

        elif 'open google' in query:
            speak("Sir, what should i search on google?")
            cm = takecommand().lower()
            webbrowser.open(f'{cm}')

        elif 'see you again' in query:
            kit.playonyt('see you again')

        else:
            speak('I cant hear what you said')
