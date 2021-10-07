import webbrowser, time

def pomodoro_method(rhythms, rhythm_length, break_length):
	'''Gebe bei 'rhythms' die Anzahl der Rhythmen ein!'''
	'''Gebe bei 'rhythm_length' die Anzahl der Länge ein!'''
	'''Gebe bei 'break_length' die Länge der Pausen ein!'''

	repeats = 0

	work_number = float(rhythm_length)*60
	break_number = float(break_length)*60

	while repeats < int(rhythms):
		time.sleep(work_number)
		print("Zeit für eine Pause!")
		webbrowser.open('https://www.youtube.com/watch?v=UceaB4D0jpo')
		time.sleep(break_number)
		print("Zeit zum Weiterarbeiten!")
		repeats += 1
		print(f"Das war deine {repeats} Pause!")

	print("Ende!")
