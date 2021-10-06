import webbrowser
import time

def pomodoro_method(rhythms, rhythm_length, break_length):
	'''Gebe bei 'rhythms' die Anzahl der Rhythmen ein!'''
	'''Gebe bei 'rhythm_length' die Anzahl (Minuten) der Länge ein!'''
	'''Gebe bei 'break_length' die Anzahl (Minuten) der Pausenlänge ein!'''

	repeats = 0

	work_number = float(rhythm_length)*60
	break_number = float(break_length)*60

	while repeats < int(rhythms):
		time.sleep(work_number)
		print("Zeit für eine Pause!")
		webbrowser.open('https://www.youtube.com/watch?v=UceaB4D0jpo')
		time.sleep(1)
		print("Zeit zum Weiterarbeiten!\n")
		repeats += 1
		print(f"Das war deine {repeats} Pause!")
		work_length = rhythm_length * repeats
		print(f"Du hast {work_length} Minuten! gearbeitet!")

	print("Ende!")