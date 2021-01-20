import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if (hour >= 0) and (hour < 12):
        speak('Good Morning! Rithhik, Do you wanna have Tea or coffee')
    elif (hour >= 12) and (hour < 18):
        speak('Good Afternoon! Rithhik, Would you like to have the lunch')
    else:
        speak('Good evening! Rithhik, Do you wanna go for a drive, you car is ready Rithhik.')


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio)
        print(f"user said: {query}\n")

    except Exception as e:
        speak('say that again please...')
        return 'none'

    return query


if __name__ == '__main__':
    speak("Hello folks, I am Awake for robotics")
    while True:
        query = takecommand().lower()
        speak('You are Rithhik, am i right')# for amazement like the presenter can present like it recognizes its master
        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences=2)
            speak("This is what i found")
            print(results)
            speak(results)
        elif "hello" in query:
            wishme()
        elif 'youtube' in query:
            speak('youtube is on its way Rithhik...')
            query = query.replace('youtube', '')
            webbrowser.open("Youtube.com")
        elif 'google' in query:
            speak('google.com is ready for you Rithhik...')
            query = query.replace('google', '')
            webbrowser.open("google.com")
        elif 'stack over flow' in query:
            speak('stackoverflow is a great platform for coders, great choice Rithhik...')
            query = query.replace('stack over flow', '')
            webbrowser.open("stackoverflow.com")
        elif 'gmail' in query:
            speak('opening your gmail account Rithhik...')
            query = query.replace('gmail', '')
            webbrowser.open("gmail.com")
        elif ('play' in query) and ("music" in query):
            music_dir = "D:\\Musics"
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))
        elif "the time" in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak('Rithhik the time is' + strtime)
        elif "open code" in query:
            speak("lets code Rithhik")
            vsc = "C:\\Users\\91934\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(vsc)
        elif ("bye friday" in query) or ("by friday" in query):
            speak('Have a good day Rithhik')
            break
        else:
            speak('You want anything else Rithhik or its done.')
