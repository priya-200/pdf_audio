import pyttsx3
import PyPDF2

engine = pyttsx3.init()
reader = PyPDF2.PdfReader('sample.pdf')
pages = reader.pages[0]
text = pages.extract_text()
engine.say(text)
engine.runAndWait()