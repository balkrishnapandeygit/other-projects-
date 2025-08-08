import speech_recognition as sr # instead of typing speech_recognition again and again we can type as sr or any name 
import webbrowser #This  is used to open web pages in  browser.
import pyttsx3  #
import datetime  #this library provides to working with date and time 
import os       #using operating system (e.g., opening files, creating directories).
import random   #random number generation
import wikipedia  #This library provides a convenient way to access and parse data from Wikipedia.
import smtplib   #This library provides an SMTP (Simple Mail Transfer Protocol) client for sending emails.


engine = pyttsx3.init('sapi5') #Initializes the text-to-speech engine with 'SAPI5' (used on Windows).
voices = engine.getProperty('voices') #Fetches the available voices in the system (male/female voices)
engine.setProperty('voices',voices[0].id) # Selects the first available voice.

def speak(audio):
    #speaks the given text
    engine.say(audio)                 #function take audio as input 
    engine.runAndWait()            

def wishme():
    #Greets user 
    hour = int(datetime.datetime.now().hour)
    if 0<= hour < 12 :
        speak("Good morning !")
    elif 12<= hour < 18 :
        speak("good afternoon !")    
    else:
        speak("good evening ! ") 

    speak( "I AM MINI AI . HOW MAY I ASSIST YOU ")    

def takecommand():
    #take voice input and returns as string
    r = sr.Recognizer()  # Creates a speech recognizer object.
    with sr.Microphone() as source:    #Opens the microphone as the audio source.
        print("Listening...")
        r.pause_threshold = 1    #control recogniser 
        audio = r.listen(source)  #Listens to the microphone and captures the audio.

    try:                                   #This function captures voice input from the microphone and converts it to text.
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')  #Uses Google's speech recognition API to convert the audio to text (language is set to English-India).
        print(f"User said: {query}\n")

    except Exception as e:
        print(e) #prints error to console.
        print("Say that again please...")
        return "None"
    return query

if __name__ == "__main__":
    wishme()
    while True :  #Creates an infinite loop to continuously listen for commands.
        query= takecommand().lower() #Creates an infinite loop to continuously listen for commands.
        if query == "none" :
            continue

        elif "wikipedia" in query:  #1st this will check wikipedia is present or not in string 
            speak("searching  wikipidia....")
            query = query.replace("wikipedia", "")   #  2nd this line replace wikipedia string and search only valid info 

            try :
                results=wikipedia.summary(query,sentences=2) #this line will search actuall wikipedia
                speak("according to wikipedia ")
                print(results)
                speak(results)
            except wikipedia.exceptions.DisambiguationError as e : #This line is for the DisambiguationError exception, which occurs when a Wikipedia search query is ambiguous and could refer to multiple pages.
                speak("please be more specific . here are some possible result :" + str(e))  
            except wikipedia.exceptions.PageError : # this line for when wikipedia will not find pages or some issue 
                speak("sorry i could not find this page ")
            except Exception as e :
                speak(f"an error occoured : {e}")
        elif "open youtube" in query:
            webbrowser.open("https://www.youtube.com")
        elif "open google"  in query :
            webbrowser.open("https://www.google.com")     
        elif "open stack overflow"  in query :
            webbrowser.open("https://stackoverflow.com") 
        elif "play music" in query:
               speak("What song or artist would you like to play?")
               music_query = takecommand() #obtain the name of the song or artist
               if music_query:
                  search_url = f"https://www.youtube.com/results?search_query={music_query}"
                  webbrowser.open(search_url)
               else: 
                 speak("I did not hear a song or artist name.")
        
        

        elif "time" in query:
         now = datetime.datetime.now()
         hour = now.strftime("%I") # 12 hour format
         minute = now.strftime("%M")
         second = now.strftime("%S")
         am_pm = now.strftime("%p")

         formatted_time = f"It is {hour} hours, {minute} minutes, and {second} seconds {am_pm}"
         print(formatted_time)
         speak(formatted_time)

        elif "date" in query:
         now = datetime.datetime.now()
         day = now.strftime("%d")
         month = now.strftime("%B") # full month name
         year = now.strftime("%Y") # four digit year

         formatted_date = f"Today's date is the {day} of {month}, {year}"
         print(formatted_date)
         speak(formatted_date)


        elif "exit" in query or "quit" in query or "stop" in query or "bye" in query:
            speak("Goodbye!")
            break

        else:
            speak("I can't understand that command. Please try again.")





          