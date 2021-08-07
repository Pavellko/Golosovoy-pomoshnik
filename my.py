from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget
import os
import sys
import speech_recognition as sr
import webbrowser
import pyautogui as pg

class App(QWidget):
	def __init__(self):
		super(App, self).__init__()
		self.start()
		self.op()




	def start(self):

		self.ui = uic.loadUi("my_diz.ui")
		self.ui.show()



	def op(self):
		self.ui.btn_1.clicked.connect(self.pr)
		self.ui.stp.clicked.connect(self.stop)

	def pr(self):
		self.ui.zx.setText("Приветики!")
		while True:
			make(command())
	def stop(self):
		sys.exit()
	


def command():
		r=sr.Recognizer()
		with sr.Microphone() as source:
			print("Говорите!")
			ex.ui.zx.setText("Говорите!")

			r.pause_threshold = 1
			r.adjust_for_ambient_noise(source, duration=1)
			audio = r.listen(source)
		try:
			zadanie=r.recognize_google(audio, language="ru-RU").lower()
			print(zadanie)

		except sr.UnknownValueError:


			zadanie = command()
		return zadanie

def make(zadanie):
		if "открой интернет" in zadanie:
			webbrowser.open("https:/mail.ru")
		elif "закройся" in zadanie:
			ex.ui.zx.setText("Хорошо, останавливаю")
			sys.exit()
		elif "напечатать" in zadanie:
			
			
			pg.typewrite(zadanie)




if __name__=='__main__':
	app = QApplication(sys.argv)
	ex=App()
	app.exec_()