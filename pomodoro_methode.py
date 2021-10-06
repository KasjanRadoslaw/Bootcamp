import webbrowser
import time

def pomodoro_method(rhythms, rhythm_length):
	'''Gebe bei 'rhythms' die Anzahl der Rhythmen ein!'''
	'''GEbe bei 'rhythm_length' die Anzahl der Länge ein!'''

	repeats = 0

	work_number = float(rhythm_length)*60

	while repeats < int(rhythms):
		time.sleep(work_number)
		print("Zeit für eine Pause!")
		webbrowser.open('https://www.youtube.com/watch?v=UceaB4D0jpo')
		time.sleep(450)
		print("Zeit zum Weiterarbeiten!\n")
		repeats += 1

	print("Ende!")