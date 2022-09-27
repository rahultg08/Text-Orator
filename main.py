import random
import PyPDF2
import pyttsx3

book = open('sample.pdf', 'rb')
pdfReader = PyPDF2.PdfReader(book)
engine = pyttsx3.init()
nopages = pdfReader.numPages
print(nopages)
for i in range(nopages):
    page = pdfReader.getPage(0)
    txt = page.extractText(page)
    engine.say(txt)

words = ['hello', 'world']
engine.say(random.choice(words))                          # Choosing random word to speak from a list of values
engine.say("Hey! I can speak")
voices = engine.getProperty('voices')
for voice in voices:
    engine.setProperty('voice', voice.id)
    engine.say("Hey! I can speak")
newVoiceRate = 120
engine.setProperty('rate', newVoiceRate)                  # Setting to lower rate of speech
engine.say("Hey! I can speak")                            # sample
rate = engine.getProperty('rate')
volume = engine.getProperty('volume')
engine.setProperty('rate', rate+50)
engine.say("Hey! I can speak")
engine.setProperty('volume', volume-0.5)
engine.say("Hey! I can speak")
engine.runAndWait()
