import pyttsx3 #for audio output
import datetime #to get the time and inturn wish the user accordingly
import speech_recognition as sr #for taking input 
import wikipedia #for searching on wikipedia 
import webbrowser #to open websites
import os #to open applictaions
import sys #to quit the program

engine = pyttsx3.init()
voices=engine.getProperty("voices")
engine.setProperty("voices",voices[1].id)#used to set the voice
rate=engine.getProperty("rate")
engine.setProperty("rate",175)#used to set the speed of talking

def speak (audio):#function to speak
    engine.say(audio)
    engine.runAndWait()
def greet():#function to greet
    hour=int(datetime.datetime.now().hour)
    if(hour<12 and hour>=0):
        speak("good morning")
    elif(hour<=17 and hour>=12):
        speak("good afternoon")
    else:
        speak("good evening")
    speak("hi i am venom how may i help you")
def take():#function to take input
    r=sr.Recognizer()
    with sr.Microphone() as source :
        print("listening........")
        speak("listening")
        r.pause_threshold= 0.5 #used to define the pause duration after a command 
        r.energy_threshold=150 #used to define mic sensitivity 
        audio=r.listen(source)

    try:
        print("recognizing........")
        speak("recognizing........")
        query=r.recognize_google(audio,language="en-in") 
        print("user said-",query)
        

    except:
        speak("say that again")
        print("say that again....")
        take()

    return query
def strt():#funtion to start the assistant
    r=sr.Recognizer()
    with sr.Microphone() as source :
        r.pause_threshold=0.5
        r.energy_threshold=150
        audio=r.listen(source)

    try:
        
        starting=r.recognize_google(audio,language="en-in") 
     
        

    except:
        
        return "None"

    return starting

    
if __name__=="__main__": #begining of the program
    while True:
        startinput=strt().lower()
        if "start" in startinput:
            greet()
            while True:
                speechinput=take().lower()
                if "wikipedia" in speechinput:#searching the query on wikipedia
                    speak("Searching wikipedia")
                    speechinput=speechinput.replace("wikipedia","")
                    result=wikipedia.summary(speechinput,sentences=3,auto_suggest=True)
                    print(result)
                    speak(result)
                    break
                elif "open google" in speechinput:#opening google
                    speak("opening google")
                    webbrowser.open("google.com")
                    break
                
                elif "open youtube" in speechinput:#opening youtube
                    speak("opening youtube")
                    webbrowser.open("youtube.com")
                    break
                
                elif "open portal" in speechinput:#opening student portal
                    speak("opening student portal")
                    webbrowser.open("portal.svkm.ac.in/usermgmt/login")
                    break
                
                elif "open mail" in speechinput:#opening mail
                    speak("opening mail")
                    webbrowser.open("mail.google.com/mail/u/1/#inbox")
                    break

                elif "open drive" in speechinput:#opening google drive
                    speak("opening drive")
                    webbrowser.open("https://drive.google.com/drive/u/0/my-drive")
                    break

                elif "open team" in speechinput:#opening msteams
                    speak("opening m s teams")
                    webbrowser.open("https://teams.microsoft.com/_#/school/conversations/General?threadId=19:567f06928a824277a5167c123641e90c@thread.tacv2&ctx=channel")
                    break
                elif "open vs code" in speechinput:#opening vs code
                    speak("opening ide")
                    os.startfile("C:\\Users\\aditv\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")#path of the software
                    break   
                elif "play music" in speechinput:#opening spotify
                    speak("opening spotify")
                    os.startfile("C:\\Users\\aditv\\AppData\\Roaming\\Spotify\\Spotify.exe")
                    break
                elif "bye" in speechinput:#quitting the program
                    speak("bye")
                    sys.exit()
                else:
                    speak("couldnt recognize command please start again")
                    continue

