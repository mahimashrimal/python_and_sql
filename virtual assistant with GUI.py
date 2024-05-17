import random
import speech_recognition as sr
import pyttsx3
import time
from time import ctime
import webbrowser
import playsound
import os
from gtts import gTTS
from tkinter import *
from PIL import ImageTk, Image


print('Say something...')
print('\n click on speak to use the assistant')
print ('\n speak what is your name for assistant name')  
print('\n speak search to search')    
print('\n speak find location to see location') 
print('\n speak play music to play songs')        
print('\n speak what is time to see current time ')
print('\n click on close to exit or say "exit"') 
r = sr.Recognizer()
speaker = pyttsx3.init()




def record_audio(ask=False):
    with sr.Microphone() as source:
        if ask:
            lee_voice(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
            print('Recognizer voice: ' + voice_data)
        except Exception:
            print('Oops something went Wrong')
        return voice_data


def lee_voice(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1, 10000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)


class Widget:  
    def __init__(self):
        root = Tk()
        root.title('nandini')  
        root.geometry('520x320')
        intro_label = Label(root, text='Say something...', font=('Century Gothic', 12))
        intro_label.pack(side='top', pady=5)

        instruction_label = Label(root, text='Click on "Speak" to use the assistant', font=('Century Gothic', 12))
        instruction_label.pack(side='top', pady=5)

        name_label = Label(root, text='Speak "What is your name?" for assistant name', font=('Century Gothic', 12))
        name_label.pack(side='top', pady=5)
        intro_label = Label(root, text='speak "search" to search', font=('Century Gothic', 12))
        intro_label.pack(side='top', pady=5)
        intro_label = Label(root, text='speak "find location" to see location', font=('Century Gothic', 12))
        intro_label.pack(side='top', pady=5)
        intro_label = Label(root, text='speak "play music" to play songs', font=('Century Gothic', 12))
        intro_label.pack(side='top', pady=5)
        intro_label = Label(root, text='speak" what is time" to see current time', font=('Century Gothic', 12))
        intro_label.pack(side='top', pady=5)
        intro_label = Label(root, text='click on close to exit or say "exit"', font=('Century Gothic', 12))
        intro_label.pack(side='top', pady=5)
        
        img = ImageTk.PhotoImage(Image.open(r"C:\Users\hp\nandini img.jpg"))
        panel = Label(root, image=img)
        panel.pack(side='right', fill='both', expand='no')
        compText = StringVar()
        userText = StringVar()
        userText.set('Your Virtual Assistant')
        
        userFrame = LabelFrame(root, text='Nandini', font=('Railways', 24, 'bold'))
        userFrame.pack(fill='both', expand='yes')
        top = Message(userFrame, textvariable=userText, bg='black', fg='white')
        top.config(font=("Century Gothic", 15, 'bold'))
        top.pack(side='top', fill='both', expand='yes')
        btn = Button(root, text='Speak', font=('railways', 10, 'bold'), bg='red', fg='white',
                     command=self.clicked).pack(fill='x', expand='no')
        btn2 = Button(root, text='Close', font=('railways', 10, 'bold'), bg='yellow', fg='black',
                      command=root.destroy).pack(fill='x', expand='no')
        lee_voice('How can I help you mahima?')
        root.mainloop()

    def clicked(self):
        print("working...")
        voice_data = record_audio()
        voice_data = voice_data.lower()
        if 'what is your name' in voice_data:
            lee_voice('My name is Nandini ')  
        if 'search' in voice_data:
            search = record_audio('What do you want to search for?')
            url = 'https://google.com/search?q=' + search
            webbrowser.get().open(url)
            lee_voice('Here is what I found: ' + search)
        if 'find location' in voice_data:
            location = record_audio('What is your location?')
            url = 'https://google.nl/maps/place/' + location + '/&amp;'
            webbrowser.get().open(url)
            lee_voice('Here is location: ' + location)
        if 'what is the time' in voice_data:
            lee_voice("mam the time is: " + ctime())
        if 'play music' in voice_data:
            music_query = record_audio('What music do you want to listen to?')
            music_url = f'https://www.youtube.com/results?search_query={music_query}+music'
            webbrowser.get().open(music_url)
            lee_voice('Playing music: ' + music_query)
        if 'exit' in voice_data:
            lee_voice('Thanks have a good day ')
            exit()
 

if __name__ == '__main__':
    widget = Widget()
    time.sleep(1)
    while 1:
        voice_data = record_audio()
        respond(voice_data)

    speaker.runAndWait()
    
