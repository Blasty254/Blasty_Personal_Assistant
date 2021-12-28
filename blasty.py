#Author @Njogu Jeff Njoroge REG:P15/136818/2019
#E-mail:njogujay.18@students.uonbi.ac.ke

import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os.path #to get contents from specified directory on your PC
import wolframalpha
import json
import requests

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id) #MALE Voice (MICROSOFT David)=0  ,, Female voice (Microsoft Zara)= 1
# Function converts text into speech
engine.setProperty('rate', 150)
def wishme ():
    hour = (datetime.datetime.now () .hour)
    if hour>0 and hour<12:
        speak('Goodmorning to you')
    elif hour>=12  and hour<18:
        speak('Good Afternoon to you')
    else:
        speak('Good Evening')
        
              

def speak(text):
    engine.say(text)
    engine.runAndWait ()
    
def takeCommand () :
    #the function will take the microphone input from the user and returns an string  (text) output
    r= sr.Recognizer() #r as record
    with sr.Microphone () as source :
        r.adjust_for_ambient_noise(source)
        print('Listening......')
        r.pause_threshold = 1
        user_audio = r.listen(source)
    try:
        print('Recognizing user input...')
        #using google api for voice recognition
        query = r.recognize_google(user_audio,language='en-in')
        print(query)
        print(f"User Said : {query}\n")
    except Exception as e:
        #we print incase there is trouble in getting the output
        print('Please say that again.....')
        speak('i did not quite catch that. Please repeat that again ')
        return "None"
    return query    

if __name__ == '__main__': #the entry point to the program
    wishme()
    print('Hello My Name is Blasty ,your new personal assistant. I am here to help you in your daily needs. What can i do for you?') 
    speak('I am Blasty ,your new personal assistant , I am here to help you in your daily needs. What can i do for you?')
    
    while True:
        query = takeCommand() .lower()
        
        #if 'what can you do' in query:
           # print('I can do a variety of things. Just try me!!')
           # speak('I can do a variety of things. Just try me')
        
        if 'wikipedia' in query :
            speak('Searching Wikipedia')
            query = query.replace('wikipedia','') #query =Kenya (remove the name wikipedia because of article error) replace with null
            query = query.replace(' ','_') #replace whitespaces to avoid page not found error
            results = wikipedia.summary(query,sentences=3) #the function searches in wikipedia and displays the result and speaks a few lines
            print(results)
            speak(results)
            
        elif 'open youtube' in query:
            query = query.replace('open','')
            speak('Opening   '+query)
            webbrowser.register('firefox',None,webbrowser.BackgroundBrowser('C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe'))
            webbrowser.get('firefox').open('https://www.youtube.com/')
            quit()
        elif 'open spotify' in query:
            query = query.replace('open','')
            speak('Opening   '+query)
            webbrowser.register('firefox',None,webbrowser.BackgroundBrowser('C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe'))
            webbrowser.get('firefox').open('https://www.spotify.com/')
            quit()
        elif 'open google' in query:
            query = query.replace('open','')
            speak('Opening   '+query)
            webbrowser.register('firefox',None,webbrowser.BackgroundBrowser('C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe'))
            webbrowser.get('firefox').open('https://www.google.com/')
            
        elif 'search' in query:
            query = query.replace('search ','')
            query = query.replace('for','')
            speak('Searching for '+query)
            query=query.replace('','+')
            webbrowser.register('firefox',None,webbrowser.BackgroundBrowser('C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe'))
            webbrowser.get('firefox').open('https://www.google.com/search?q='+query)
            quit()
        
        
        elif 'on youtube' in query:
            query = query.replace('search for ','')
            query = query.replace('for','')
            speak('Searching for '+query)
            query=query.replace('','+')
            webbrowser.register('firefox',None,webbrowser.BackgroundBrowser('C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe'))
            url=('https://www.youtube.com/search?q='+query)
            webbrowser.get('firefox').open(url)
            quit()
            
        elif 'time' in query:
            ctime = datetime.datetime.now().strftime('%I:%M:%p')
            print('It is currently :' +ctime)
            speak(f'The Time is {ctime}')
        
        elif 'ask questions' in query:
            print('i can answer to computational and geographical questions. What would you like to ask?')
            speak('i can answer to computational and geographical questions. What would you like to ask?')
            question = takeCommand()
            app_id = 'PU3HK2-WGGU3EU538'
            #create an ionstance of Client Class
            client = wolframalpha.Client(app_id)
            res= client.query(question)
            for i in res.results:
                print(i.text)
                speak(i.text)
                
        elif 'weather' in query:
            api_key ='0dcd58fbd91298db20b769ac6c94e07a'
            base_url = 'api.openweathermap.org/data/2.5/weather?'
            speak('Sure , which city weather would you like to know ?')
            city_name = takeCommand()
            city_name = city_name.replace('','%20')
            complete_url = base_url + 'q=' + city_name + '&appid' + api_key
            response = requests.get(complete_url)
            x = response.json()
            if x["code"]!="404":
                y = x["main"]
                current_temperature = y["temp"]
                current_temperature = int(current_temperature - 273)
                print(current_temperature )
                city_name = city_name.replace('%20','')
                speak('Temperature in'+city_name+ 'is'+ str(current_temperature)+ 'degrees celsius')
                
            
            
            
        
            
            
            
        
        elif   'play music' in query:
            speak('Playing your fire  Music playlist')
            music_dir= 'C:\\Personal_Voice_Assistant\\Music'
            music= os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,music[4]))
            quit()
            
                 
        elif 'exit' in query:
            speak('Thank You. Going offline now')
            quit()
        

