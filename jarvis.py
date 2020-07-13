import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
engine=pyttsx3.init("sapi5")
voices=engine.getProperty("voices")
#print(voices[1].id)
engine.setProperty("voice",voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>0 and hour<12:
        speak("good morning")
    elif hour>=12and hour<18:
        speak("good afternoon")
    elif hour>18 and hour<=24:
        speak("good evening")
    speak("I am jarvis sir Please tell me how may i help you ")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognising")
        query=r.recognize_google(audio,language="en-in")
        print(f"user said{query}\n")
    except Exception as e:
        #print(e)
        print("say it again")
        return "None"
    return query
if __name__ == '__main__':
    wishMe()
    if 1:
    # while True:
        query=takeCommand().lower()
        if 'wikipedia' in query:
            speak("searching wikipedia...")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia-")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            speak("yeh open youtube")
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            speak("yeh open youtube")
            webbrowser.open("google.com")
        elif 'play music' in query:
            music_dir='C:\\Users\\Hp\\PycharmProjects\\ firstprog\\music'
            song=os.listdir(music_dir)
            #print(song)
            os.startfile(os.path.join(music_dir,song[0]))
        elif 'the time' in query:
            str=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir the time is {str}")
        elif 'open' in query:
            codde='C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.1\\bin\\pycharm64.exe'
            os.startfile(codde)
        elif 'exit' in query:
            speak("ok i exit it")
            exit()



