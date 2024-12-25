import speech_recognition as sr # type: ignore
import pyttsx3 # type: ignore
import pywhatkit # type: ignore
import datetime
import wikipedia # type: ignore
import pyjokes # type: ignore

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Use a female voice; change to voices[0].id for a male voice

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            listener.adjust_for_ambient_noise(source)
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'john' in command:
                command = command.replace('john', '')
                print(command)
                return command
    except sr.UnknownValueError:
        talk("Sorry, I did not catch that. Please repeat.")
    except sr.RequestError:
        talk("Sorry, my speech service is down.")
    except Exception as e:
        print(f"Error: {e}")
    return ""

def run_assistant():
    command = take_command()
    if command:
        print(command)
        if 'play' in command:
            song = command.replace('play', '')
            talk('Playing ' + song)
            pywhatkit.playonyt(song)
        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            talk('The current time is ' + time)
        elif 'who is' in command:
            person = command.replace('who is', '')
            info = wikipedia.summary(person, 1)
            talk(info)
        elif 'date' in command:
            today = datetime.datetime.today().strftime('%B %d, %Y')
            talk("Today's date is " + today)
        elif 'day' in command:
            today = datetime.datetime.today().strftime('%A')
            talk("Today is " + today)
        elif 'joke' in command:
            talk(pyjokes.get_joke())
        elif 'what is your name' in command:
            talk("I am your assistant created in Python.")
        elif 'how are you' in command:
            talk("I'm a chatbot, so I don't have feelings, but thanks for asking!")
        elif 'bye' in command:
            talk("Goodbye! Have a great day!")
            exit()
        else:
            talk('Sorry, I did not understand that. Can you please repeat?')

while True:
    run_assistant()
