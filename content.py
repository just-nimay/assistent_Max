import pyttsx3
import speech_recognition as sr
import os
from playsound import playsound

engine = pyttsx3.init()

mic = sr.Microphone(device_index=0)

list_mic = sr.Microphone.list_microphone_names()
for i in range(0, len(list_mic)):
	print(i, list_mic[i])

r = sr.Recognizer()

run = True
while run:
	
	def home():
		playsound('und.WAV', False)
		os.system('open /Applications/Spotify.app')
		os.system('open /Applications/Sublime_Text.app')
		os.system(' open /Applications/Telegram.app')
		os.system(' open /Applications/Utilities/Terminal.app')


		

	def command(word):
		if word == 'я дома':
			home()
			
		elif word == 'выход':
			run = False
			return run
			

		
	
	with mic as sourse:
		print('говорите...')
		audio = r.listen(sourse)
		
		
	try:
		a = r.recognize_google(audio, language="ru-RU")
		print('вы сказали: ' + a)
		command(a.lower())
		answ = command(a.lower())
		if answ == False:
			run = False
		
				
	except sr.UnknownValueError:
		print('я не поняла что вы сказали, повторите пожалуйста')
		

	except sr.RequestError as e:
		print('ошибка соединения с сервером ')
	

'''
	













