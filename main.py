import datetime
from email.message import EmailMessage 
from secret import senderemail,password
import smtplib
import  webbrowser as we
from time import sleep
import pyautogui
import requests
from newsapi import NewsApiClient
import pywhatkit
import clipboard
import pyjokes
import time as ti
import psutil
import pyttsx3 #text to speech convertion
import speech_recognition as sr




def inputCommand():
    
    r = sr.Recognizer()
    query = ""
    with sr.Microphone(device_index=2) as source:
        print("Listening...")
        r.pause_threshold = 1
        try:
            query = r.recognize_google(r.listen(source), language="en-IN")
            
        except Exception as e:
            print(e)
            output("Say that again please...")
    return query


def output(out):
    
    engine.say(out)
    engine.runAndWait()

user="Aiswarya"
assistant = "Jarvis"
engine = pyttsx3.init()
voices = engine.getProperty("voices")
# engine.setproperty("voice",voices[0].id) ---->male
engine.setProperty("voice",voices[0].id)  #-->Femaale
output(f"Hello this is {assistant}")




def greet():
    hour =datetime.datetime.now().hour
    if(hour >= 6) and (hour < 12 ):
        output(f"Good morining {user}")
    elif(hour >= 12) and (hour < 16 ):
        output(f"Good After Noon {user}")
    elif(hour >= 18) and (hour < 21 ):
        output(f"Good morining {user}")
    else:
        output("How may I assist you?")

def sendEmail():
    email_list={
        "test":"mohigix759@bio123.net"
        }
    try:
        email = EmailMessage()
        output("To whom do you want to send e-mail?")
        name = inputCommand().lower()
        email["To"] = email_list[name]
        output("What is the subject of your e-mail?")
        email["Subject"] = inputCommand()
        email["From"] = senderemail
        output("What should I say?")
        email.set_content(inputCommand())
        s = smtplib.SMTP("smtp.gmail.com",587)
        s.starttls()
        s.login(senderemail,password)
        s.send_message(email)
        s.close()
        output("E-mail has been send")
    except Exception as e:
        print(e)
        output("Unable to send the E-mail")


def sendWhatsappMsg():
    user_list = {
        "test1":"+91"
    }
    try:

        output("To whom do you want to send message?")
        name = inputCommand().lower()
        output("What is the message?")
        we.open("https://web.whatsapp.com/send?phone=" + user_list[name] +"&text=" +inputCommand())
        sleep(6)
        pyautogui.press("enter")
        output("Message send")
    except Exception as e:
        print(e)
        output("Unable to send the message")


def weather():
    city = 'Thrissur'
    res = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=API&units=metric").json()
    temp  = res["weather"][0]["description"]
    temp2  = res["main"]["temp"]
    output(f"Temparature is {format(temp2)} degree Celsius\nWeather is {format(temp)}")


def news():
    newsapi = NewsApiClient(api_key ="API")
    output("In which topic do you want news about?")
    topic  = inputCommand().lower()
    data  = newsapi.get_top_headlines(q=topic,language='en',page_size =5)
    newsdata = data['articles']
    for y in newsdata:
        output(y["description"])



def idea():
    output("What is your idea?")
    data = inputCommand().title()
    output("You said me to remember this Idea:" +  data)
    with open("data.txt","a",encoding="Utf-8") as r:
        print(data,file= r)
greet()



while True:
    query = inputCommand().lower()
    if ("time" in query):
        output("Current time is:" + datetime.datetime.now().strftime("%I:%M"))
    elif ("date" in query ):
        output("Current date is " + str(datetime.datetime.now().day)+" " +
        str(datetime.datetime.now().month())+" " + str(datetime.datetime.now().year))
    elif ("email" in query):
        sendEmail()
    elif ("message" in query):
        sendWhatsappMsg()
    elif ("search" in query):
        output("What do you want to search?")
        we.open("https://www.google.com/search?q="+inputCommand())
    elif ("youtube" in query):
        output("What do you want to search on youtube?")
        pywhatkit.playonyt(inputCommand())
    elif("weather" in query):
        weather()
    elif("news" in query):
        news()
    elif("read" in query):
        output(clipboard.paste())
    elif("covid" in query):
        r = requests.get("https://coronavirus-19-api.herokuapp.com/all").json()
        output(f'Confirmed cases: +{r["cases"]} \n "Deaths:"+{r["deaths"]} \n "Recovered:"+{r["recovered"]}' )
    elif ("joke" in query):
        output(pyjokes.get_joke())
    elif("idea" in query):
        idea()
    elif("do you know" in query):
        idea = open("data.txt","r")
        output(f"You said me to remember these ideas:\n{idea.read()}")
    elif("screenshot" in query):
        pyautogui.screenshot(str(ti.time()) +".png").show()
    elif("cpu" in query):
        output(f"CPU is at {str(psutil.cpu_percent())}")
    elif("What can you do" in query):
        list_commands={
            "Date and time":"what time/date its is?",
            "Email":"Send email",
            "Whatsapp Message":"Send message",
            "Search":"Search about topic",
            "Search youtube":"Play video on youtube",
            "Weather":"What weather is in kochi?",
            "News/Read":"news about covid/read about covid",
            "Covid updates":"Tell covid updates",
            "Joke":"Tell Me a Joke",
            "Idea":"Remeember these idea",
            "Screenshot":"Take screenshot",
            "CPU":"CPU is at..",
            "Offline":"Go offline"
        }
        ans = """I can do lots of things, for example you can ask me time, date, weather in your city,
        I can open websites for you, take screenshots and more. See the list of commands-"""
        output(ans)
        print(list_commands)
    elif("offline" in query):
        hour = datetime.datetime.now().hour
        if (hour>=21) and (hour <6 ):
            output(f"Good night {user}.Have a good sleep!!")
        else:
            output(f"Bye {user}")
        quit()


    
        

