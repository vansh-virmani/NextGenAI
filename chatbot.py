from datetime import datetime
import speech_recognition as sr
import pyttsx3
import webbrowser
import requests
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Speed percent (can go over 100)
engine.setProperty('volume', 0.9)  # Volume 0-1
def speek(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    rec = sr.Recognizer() #access microphone 
    with sr.Microphone() as source:
        print("Listening...")
        audio = rec.listen(source)
    try:
        message = rec.recognize_google(audio) #recognize voice
        print(f"You said: {message}")
        return message.lower()
    except sr.UnknownValueError:
        print("Sorry, I did not understand that.")
        return ""
greet_msgs=["hi","hello","hi there","hey","hello there"]
date_msgs=["date","tell me date","today's date"]
time_msgs=["time", "tell me time", "current time"]
news_msgs=["tell  me news","news","headlines"]
temp_msgs=["tell me temperature", "temp" , "temperature now", "weather"]
def get_news():
    url= "https://newsapi.org/v2/top-headlines?country=us&apiKey=695e07af402f4b119f0703e9b19f4683"
    response=requests.get(url)
   
    data=response.json()
    articles = data['articles']
    for i in range(len(articles)):
        print(articles[i]['title'])
def get_location():
    url="http://ip-api.com/json/?fields=lat,lon"
    response=requests.get(url)
    

    data=response.json()
    return data['lat'], data['lon']


def get_temp():
    lat,lon=get_location()
    # return print(lat,lon)

    url=f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m"
    # print(url)
    response=requests.get(url)
    
    data=response.json()
    current = data["current"]
    # print(current)

    for key, value in current.items():
          if key == "temperature_2m":
              ans=value
              print(ans)
              break
    
     

        

    

chat=True
    #Corpus - set of greetings dataset 
while chat:
    # user_msg = input("Enter your message : ").lower()
    user_msg= listen()
    if user_msg in greet_msgs:
        print("hello User, How may I help you?")
    elif user_msg in date_msgs:
        print(f"Today's date is  {datetime.now().date()}")
    elif user_msg in time_msgs:
        current_time= datetime.now().time()
        print("time is:", current_time.strftime("%I:%M:%S %p"))
    elif "open" in user_msg:
        website_name= user_msg.split()[-1]

        webbrowser.open(f"https://www.{website_name}.com/")
    elif "calculate" in user_msg:
        expression=user_msg.split()[-1]
        result=eval(expression)
        print("result is", result)
    elif user_msg in news_msgs:
        get_news()
    elif user_msg in temp_msgs:
        get_temp()
    elif user_msg == "bye":
        print("Thanks for connecting!")
        chat=False
    
    else:
        print(" I cannot understand")