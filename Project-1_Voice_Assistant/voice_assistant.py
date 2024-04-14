""" Voice Assistant Program
    Primary Tasks:
    - Recognize and execute commands like time, date, search, email.
    - Basic interaction using speech recognition and text-to-speech.

    Advanced Tasks:
    - Fetch weather information based on user input.
    - Answer general knowledge questions using Wikipedia.
    - Set reminders for specific tasks."""
    
# Function importing

import webbrowser, wikipedia, requests, datetime, smtplib, pyttsx3
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import speech_recognition as sr
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Initializations
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Function to speak out the given text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to recognize speech input
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        audio = recognizer.listen(source)

        try:
            print("Recognizing...")
            query = recognizer.recognize_google(audio, language='en-US')
            print("User said:", query)
            return query.lower()
        except sr.UnknownValueError:
            speak("Sorry, I didn't get that. Can you please repeat?")
            return listen()
        except sr.RequestError as e:
            speak("Sorry, I couldn't process your request. Please try again later.")
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
            return None

# Function to perform tasks based on user's voice command
def perform_task(query):
    if "hello" in query:
        speak("Hello! How can I assist you today?")
    elif "time" in query:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak("The current time is " + current_time)
    elif "date" in query:
        current_date = datetime.datetime.now().strftime("%A, %B %d, %Y")
        speak("Today's date is " + current_date)
    elif "search" in query:
        speak("What would you like me to search for?")
        search_query = listen()
        if search_query:
            url = "https://www.google.com/search?q=" + search_query.replace(" ", "+")
            webbrowser.open(url)
            speak("Here are the search results for " + search_query)
    elif "email" in query:
        send_email()
    elif "weather" in query:
        get_weather()
    elif "reminder" in query:
        set_reminder()
    elif "question" in query:
        answer_question()
    elif "sooromeen eessa jirti?" in query:
        speak("Si bira teessee Feesbuukii ilaalti")
    elif "exit" in query or "quit" in query:
        speak("Goodbye!")
        exit()
    else:
        speak("Sorry, I couldn't understand that command.")

# Function to send an email
# Function to send an email
def send_email():
    recipient = os.getenv("RECIPIENT_EMAIL")  # Email address of the recipient
    subject = "Sending a voice assistant development"
    content = """\
    <html>
        <body>
            <p>Dear Demo,</p>
            <p>This is to send you my recent development called voice assistant.</p>
            <p>You can find it on GitHub: <a href="https://github.com/DemisoDaba/Oasis-Infobyte-Python-Intern/blob/main/Project-1_Voice_Assistant/voice_assistant.py">Voice Assistant Development</a>.</p>
            <p>Best regards,<br/>Demiso D.</p>
        </body>
    </html>
    """

    # Gmail SMTP server configuration
    gmail_user = os.getenv("GMAIL_USER")
    gmail_password = os.getenv("GMAIL_PASSWORD")

    # Create message container - the correct MIME type is multipart/alternative
    msg = MIMEMultipart('alternative')
    msg['From'] = gmail_user
    msg['To'] = recipient
    msg['Subject'] = subject

    # Attach HTML content
    msg.attach(MIMEText(content, 'html'))

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(gmail_user, recipient, msg.as_string())
        server.close()
        speak("Email has been sent.")
    except Exception as e:
        print(e)
        speak("Sorry, I couldn't send the email.")

# Function to get the weather
def get_weather():
    api_key = os.getenv("WEATHER_API_KEY")
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    speak("Please provide the city name.")
    city = listen()

    if city:
        complete_url = f"{base_url}q={city}&appid={api_key}"
        
        try:
            response = requests.get(complete_url, timeout=10)  # Set a timeout of 10 seconds
            response.raise_for_status()  # Raise an exception 
            data = response.json()

            if data["cod"] != "404":
                city_name = data["name"]
                country_code = data["sys"]["country"]
                temperature = round(data["main"]["temp"] - 273.15, 1)  # Convert Kelvin to Celsius
                humidity = data["main"]["humidity"]
                pressure = data["main"]["pressure"]

                speak(f"The current temperature in {city_name}, {country_code} is {temperature}°C.")
                speak(f"The humidity is {humidity}%.")
                speak(f"The pressure is {pressure}hPa.")
            else:
                speak("City not found. Please try again.")
        except requests.exceptions.ConnectTimeout:
            speak("Sorry, there was a timeout while connecting to the weather service. Please try again later.")
        except requests.exceptions.HTTPError:
            speak("Sorry, there was an error while retrieving weather data. Please try again later.")
        except Exception as e:
            speak(f"Sorry, an unexpected error occurred: {str(e)}")
    else:
        speak("Sorry, I didn't get the city name. Please try again.")

# Function to set a reminder
def set_reminder():
    speak("What do you want to be reminded about?")
    reminder = listen()
    speak("When should I remind you? Please specify the time.")
    time = listen()

# Function to answer a general knowledge question
def answer_question():
    speak("What do you want to know?")
    question = listen()
    speak("Let me find the answer for you.")
    try:
        result = wikipedia.summary(question, sentences=1)
        speak("According to Wikipedia, " + result.split('.')[0] + ".")
    except wikipedia.exceptions.PageError:
        speak("Sorry, I couldn't find any information about that.")
    except wikipedia.exceptions.DisambiguationError as e:
        speak("There are multiple results for that query. Can you please be more specific?")
    except Exception as e:
        speak("Sorry, I encountered an error while processing your request.")
# Main function to continuously listen for commands
def main():
    speak("Hello! I'm your advanced voice assistant. How can I assist you today?")
    while True:
        query = listen()
        if query:
            perform_task(query)

if __name__ == "__main__":
    main()
