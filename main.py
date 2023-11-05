import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
 

engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
       engine.say(audio) 
       engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
         speak("Good Afternoon")
    else:
         speak("Good Evening")

    speak("How may i help you")

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening . . .")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') 
        print(f"User said: {query}\n")  

    except Exception as e:
        # print(e)    
        print("Say that again please . . .")  
        return "None" 
    return query


if __name__=="__main__" :
    
    wishme()

    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:  
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2) 
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak('Opening Youtube...')
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak('Opening Google...')
            webbrowser.open("google.com")

        elif 'open github' in query:
            speak('Opening Github...')
            webbrowser.open("github.com")

        elif 'open whatsapp' in query:
            speak('Opening whatsapp...')
            webbrowser.open("web.whatsapp.com")

        elif 'open telegram' in query:
            speak('Opening telegram...')
            webbrowser.open("https://web.telegram.org/k/")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"The time is {strTime}")
