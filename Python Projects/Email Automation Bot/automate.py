# ANAYAT KHAN CSE-H

import smtplib #
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage

listener = sr.Recognizer()
engine = pyttsx3.init()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def get_info():
    try:
        with sr.Microphone() as source:
            print("Listen...")
            voice = listener.listen(source)
            info = listener.recognize_google(voice)
            print(info)
            return info.lower()
    except:
        pass

def send_email(reciever, subject, message):

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('akanayat0@gmail.com', 'Blogger@321')
    email = EmailMessage()
    email['From'] = 'akanayat0@gmail.com'
    email['To'] = reciever
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)

email_list = {

    'pink': 'anayat0khan@gmail.com',
    'nk': 'nftdesire@gmail.com'
}

def get_email_info():

    talk("To whom you want to send email")
    name = get_info()
    reciever = email_list[name]
    print(reciever)
    talk("what is the subject of your email?")
    subject = get_info()
    talk("Tell me the text in your email")
    message = get_info()
    send_email(reciever, subject, message)

    talk("Hey, lazy dude. Your email is sent")
    talk("Do you want to send more email?")
    send_more = get_info()
    if 'yes' in send_more:
        get_email_info()

get_email_info()

