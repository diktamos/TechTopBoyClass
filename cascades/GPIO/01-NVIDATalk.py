import os
import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate',150)
engine.setProperty('voice','english+f4')
text = 'Get Ready Player 1. The play will be Rough. Are you Ready to Rumble!?'

engine.say(text)
engine.runAndWait()