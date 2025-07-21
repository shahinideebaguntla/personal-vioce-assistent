import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import pywhatkit

# Initialize the text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Speed of voice

# Speak out loud
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Greet the user
def wish_user():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am your assistant. How can I help you?")

# Listen to user voice
def take_command():
    listener = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening...")
        audio = listener.listen(source)

    try:
        command = listener.recognize_google(audio)
        command = command.lower()
        print("🗣️ You said:", command)
        return command
    except:
        speak("Sorry, I didn't catch that. Please repeat.")
        return ""

# Main assistant logic
def run_assistant():
    wish_user()
    while True:
        command = take_command()

        if "time" in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            speak(f"The time is {time}")

        elif "who is" in command:
            person = command.replace("who is", "")
            info = wikipedia.summary(person, sentences=2)
            print(info)
            speak(info)

        elif "play" in command:
            song = command.replace("play", "")
            speak(f"Playing {song}")
            pywhatkit.playonyt(song)

        elif "exit" in command or "stop" in command:
            speak("Goodbye! Have a nice day.")
            break

        else:
            speak("I didn't understand that. Can you say it again?")

# Start the assistant
run_assistant()
