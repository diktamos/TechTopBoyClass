import os
from gtts import gTTS

myText = 'Get Ready Player 1. The play will be rough. Are you Ready to Rumble?'

myOutput = gTTS(text = myText, lang='en',slow=False)
myOutput.save('talk.mp3')
os.system('mpg123 talk.mp3')