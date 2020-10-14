# use pyttsx3 for text to speech conversion
import pyttsx3

# init function to get an engine instance for the speech synthesis


engine = pyttsx3.init()
engine.say('Hello sir, how may I help you, sir.')
engine.runAndWait()
