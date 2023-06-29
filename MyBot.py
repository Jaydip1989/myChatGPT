import speech_recognition as sr
import os
import webbrowser
import datetime
import openai
import random
from config import apikey



def say(text):
    os.system(f'say {text}')

def ai(prompt):
    openai.api_key = apikey

    text = f"OpenAI response for prompt: {prompt} \n ************************ \n\n"

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt = prompt,
        temperature = 0.7,
        max_tokens = 256,
        top_p = 1,
        frequency_penalty = 0,
        presence_penalty = 0
    )
    #print(response['choices'][0]['text'])
    text += response['choices'][0]['text']

    if not os.path.exists("Openai"):
        os.mkdir("OpenAI")

    with open(f"OpenAI/{''.join(prompt.split('AI')[1:])}.txt", 'w') as f:
        f.write(text)

chatStr = ""
def chat(query):
    global chatStr
    openai.api_key = apikey
    print(chatStr)
    chatStr += f"Dipit: {query} \n Deep: "
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt = chatStr,
        temperature = 0.7,
        max_tokens = 256,
        top_p = 1,
        frequency_penalty = 0,
        presence_penalty = 0
    )
    say(response['choices'][0]['text'])
    chatStr += f"{response['choices'][0]['text']}\n"
    return response['choices'][0]['text']

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.6
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f'User said: {query}')
            return query
        except Exception as e:
            return "Some Error Occurred. Sorry from Deep"
        
if __name__ == '__main__':
    say('Deep A.I')
    while True:
        print('Listening...')
        query = takeCommand()


        sites = [["youtube", "https://www.youtube.com"],["wikipedia", 'https://www.wikipedia.com'],
                 ['google', 'https://www.google.com']]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]} Sir....")
                webbrowser.open(site[1])

        if "open music" in query:
            musicPath = "/Users/dipit/TestMusic/Desperate.mp3"
            os.system(f'open {musicPath}')
        
        if "the time" in query:
            strfTime = datetime.datetime.now().strftime("%H:%M:%S")
            say(f"Sir the time right now is {strfTime}")

        if "open facetime".lower() in query.lower():
            os.system(f'open /System/Applications/FaceTime.app')

        if "Using AI".lower() in query.lower():
            ai(prompt = query)

        if "Deep Quit".lower() in query.lower():
            exit()
        
        if "reset chat".lower() in query.lower():
            charStr = ""

        else:
            print('Chatting...')
            chat(query)




        #say(query)