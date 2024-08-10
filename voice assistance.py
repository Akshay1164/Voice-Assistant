import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
import pyjokes
import os
import random
import pyautogui


engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time_():            #to know the time according to the pc
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("The current time is")
    speak(Time)

def date_():            #to know the date according to the pc
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    day = datetime.datetime.now().day
    speak("The current year is")
    speak(year)
    speak("The current month is")
    speak(month)
    speak("The current day is")
    speak(day)

def wish():            #initialization
    time_()
    date_()

    hour = datetime.datetime.now().hour

    if hour>=5 and hour <12:
        speak("Good morning")
    if hour>=12 and hour<18:
        speak("Good afternoon")
    if hour>=18 and hour<24:
        speak("Good evening")
    if hour>=1 and hour<5:
        speak("Good night")

    speak("I am waiting to help you")

def TakeCommand():          #take command from the user through mic
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recogninzing....")
        query = r.recognize_google(audio, language='en-US')
        print(query)

    except Exception as e: #if nothing is in the query and the mic value is 1
            print(e)
            print("Say that again please..")

            return "None"
    return query

def joke():
    speak(pyjokes.get_joke())

def screenshot():
    img = pyautogui.screenshot()
    img.save('C:/Users/varun/Desktop/screenshot.png')

if __name__=="__main__":

    wish()

    while True:
        query = TakeCommand().lower()           
        
        #all commands are converted into lower case for easy understanding(for the pc)

        
        if 'what can you do' in query:
            speak("I can open apps and stuff, i can search and answer any of you question, i can read the answer if you want to")
            speak('i can open the site you tell me to open, i can take a screenshot if you want to')
            speak('i can tell the time and date whenever you want me to tell you')
            speak('i can search places, tell you jokes, remember something you tell, calculate aynthing you give me')

        
        elif 'who are you' in query:
            speak('I am the voice assistant')

        if 'time' in query:
            time_()

        elif 'date' in query:
            date_()

        elif 'tell me' in query:
            speak("searching...")
            query=query.replace('wikipedia','')
            result = wikipedia.summary(query)
            print(result)
            speak(result)

        elif 'search in chrome' in query:
            speak('What should I search?')
            chromepath = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'

            search = TakeCommand().lower()
            wb.get(chromepath).open_new_tab(search+'.com') #only works with websites with .com postfix

        elif 'search in youtube' in query:
            speak("What should I search?")
            search_Term = TakeCommand().lower()
            speak("Here we go to YOUTUBE!!")
            wb.open('https://www.youtube.com/results?search_query='+search_Term)

        elif 'search in google' in query:
            speak('What should i search for you?')
            search_Term = TakeCommand().lower()
            speak('Searching...')
            wb.open('https://www.google.com/search?q='+search_Term)

        elif 'what' in query:
            query = query.replace("what is", "")
            speak("you asked me that what is"+query)
            wb.open_new_tab("https://www.google.com/search?q="+query)

        elif 'which' in query:
            query = query.replace("what is", "")
            speak("you asked me that "+query)
            wb.open_new_tab("https://www.google.com/search?q="+query)

        elif 'who' in query:
            query = query.replace("what is", "")
            speak("you asked me that"+query)
            wb.open_new_tab("https://www.google.com/search?q="+query)

        elif 'joke' in query:
            joke()

        elif 'go offline' in query:
            speak("Going offline")
            quit()  
        
        elif 'open steam' in query:
            speak("Opening steam")
            steam = r'D:/Steam/steam.exe'
            os.startfile(steam)
        
        elif 'write a note' in query:
            speak("What should i write?")
            notes = TakeCommand()
            file = open('note.text','w')
            speak('should I include date and time?')
            ans = TakeCommand()
            if 'yes' in ans or 'sure' in ans:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                file.write(strTime)
                file.write(':-')
                file.write(notes)
                speak("Done taking notes")
            
            if 'notes' in ans:
                file(notes)

        elif 'show note' in query:
            speak('showing notes')
            file = open('note.txt','r')
            print(file.read())
            speak(file.read())

        

        elif 'remember' in query:
            speak("What shoud I remember?")
            memory = TakeCommand()
            speak("You asked me to remember that"+memory)
            remember = open('memory.txt.','w')
            remember.write(memory)
            remember.close()

        elif 'tell me what i asked you to remember' in query:
            remember = open('memory.txt','r')
            speak('you asked me to remember that')
            speak(remember.read())

        elif 'where' in query:
            query = query.replace("where is", "")
            location = query
            speak("you asked to locate"+location)
            wb.open_new_tab("https://www.google.com/maps/place/"+location)

        

        elif 'sign out' in query:
            os.system("shutdown -l")
        elif 'restart' in query:
            os.system("shutdown /r /t 1")
        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")
