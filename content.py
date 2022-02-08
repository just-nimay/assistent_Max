import pyttsx3
import speech_recognition as sr
import os
from playsound import playsound

engine = pyttsx3.init()


mic = sr.Microphone(device_index=0)

'''
list_mic = sr.Microphone.list_microphone_names()
for i in range(0, len(list_mic)):
	print(i, list_mic[i])
'''
r = sr.Recognizer()

opts = {
	'alias': ('макс', "мася", "максим", "слушай"),
	'comnd': ('создай', 'создать'),
	'folder': ('папка', 'папку', 'папки'),
	'dirs': ('рабоч','стол'),
	'file': ('файл', 'документ'),
	'extension': ('txt', 'py', 'html', 'css', 'js')
}

run = True
while run:
	
	def home():
		os.system('open und.WAV')
		os.system('open /Applications/Spotify.app')
		os.system('open /Applications/Sublime_Text.app')
		os.system('open /Applications/Telegram.app')
		os.system('open /Applications/Utilities/Terminal.app')
		os.system('open /Applications/GitHub-darwin-x64/GitHub.app')

	def search(request, word):
		print('поиск индекса у слова...')
		just = request.split()
		j = int(just.index(word)) + 1
		return(j)

	def make_dir(name_of_fdr):
		print('в запросе не найдена дериктория!')
		inp_dir = input('где сохранить файл?: ')
		if 'рабоч' in inp_dir and 'стол' in inp_dir:
			directory = '/Users/nimaymac/Desktop/'
			
								
		elif 'загруз' in inp_dir:
			print('определено создание в папке загрузки')
			directory = '/Users/nimaymac/Downloads/'
			

		elif 'фото' in inp_dir:
			print('определено создание в папке фото')
			directory = '/Users/nimaymac/Pictures/'
			

		elif'видео' in inp_dir:
			print('определено создание в папке видео')
			directory = '/Users/nimaymac/Movies/'
			

		elif 'докум' in inp_dir:
			print('определено создание в папке документы')
			directory = '/Users/nimaymac/Documents/'
			

		else:
			print('директория не удалось распознать...')
			while True:
				choice = input('создать новый раздел в программе?  Y/N:').lower()
				if 'y' in choice:
					print('эта опция будет добавлена позже...')
					break
				elif 'n' in choice:
					break
				else:
					print('вы введи неверное значение') 
					continue
		return directory

	def command(request):
		print(request)
		predl = request.split()
		j = False
		n = False
		if 'создай' in request or 'создать' in request:
			print('обнаружена команда создать!')
			j = True
			for i in predl:
				print('состояние на создание: ', j)
				#создание файла
				if i in opts['file'] and j == True:
					print('выполсянется создание файла')
					ind = int(search(request, i))
					name = predl[ind]
					print('название файла: ', name)
					n = True

				if i in opts['extension'] and j == True :
					print(i, 'есть в opts[]')
					for q in opts['extension']:
						if i == q:
							ext = q
							print('расширение: ', ext)
							print('название файла: ', name)
							name_with_ext = name + ext
						else:
							pass
				elif '.' in request and j == True and n == True:
					print('файл сохранится как ', name)

				if i not in opts['dirs'] and n == True:
						dir_of_file =  make_dir(name)
						print('файл будет созданен по пути: ',dir_of_file)
				elif i in opts['dirs'] and n == True:
					pass
				#создание папки
				if i in opts['folder'] and j == True:
					ind = int(search(request, i))
					name_of_fdr = predl[ind]
					print('название папки: ', name_of_fdr)	
					
				if 'рабоч' in i and 'стол' in request:
					print('определено создание на рабочем столе')
					dir_desktop = True
					dir_folder = False
					directory = '/Users/nimaymac/Desktop/'
					print("if 'рабоч' in request and 'стол' in request is worked!")
					os.system('mkdir '+ directory + name_of_fdr)
					print('успешно!')

				elif i == 'папке':
					ind = int(search(request, i))
					name_dirFolder = predl[ind]
					dir_folder = True
					dir_desktop = True
					print("определено создание в папке")
								
					if name_dirFolder == 'загрузки':
						print('определено создание в папке загрузки')
						directory = '/Users/nimaymac/Downloads/'
						os.system('mkdir '+ directory + name_of_fdr)
						print('успешно!')

					elif name_dirFolder == 'фото':
						print('определено создание в папке фото')
						directory = '/Users/nimaymac/Pictures/'
						os.system('mkdir '+ directory + name_of_fdr)
						print('успешно!')

					elif name_dirFolder == 'видео':
						print('определено создание в папке видео')
						directory = '/Users/nimaymac/Movies/'
						os.system('mkdir '+ directory + name_of_fdr)
						print('успешно!')

					elif name_dirFolder == 'документы':
						print('определено создание в папке документы')
						directory = '/Users/nimaymac/Documents/'
						os.system('mkdir '+ directory + name_of_fdr)
						print('успешно!')
		elif request == 'выход':
			run = False
			return run

		elif request == 'я дома':
			home()
		elif request == 'открой finder':
			os.system('open  /System/Library/CoreServices/Finder.app')

		else:
			print('я пока что не обучен такому...')

	cmd = command(input('введите команду: '.lower()))
	if cmd == False:
		run = False

	'''
	with mic as sourse:
		r.adjust_for_ambient_noise(sourse)
		engine.say('говорите...')
		engine.runAndWait()
		audio = r.listen(sourse)
		
		
	try:
		a = r.recognize_google(audio, language="ru-RU")
		print('вы сказали: ' + a)
		answ = command(a.lower())
		if answ == False:
			run = False
		
				
	except sr.UnknownValueError:
		print('я не поняла что вы сказали, повторите пожалуйста')
		

	except sr.RequestError as e:
		print('ошибка соединения с сервером ')
	'''


	

