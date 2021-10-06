import webbrowser
import time

repeats = 0

while repeats < 5:
	time.sleep(5400)
	print("Zeit für eine Pause!")
	webbrowser.open('https://www.youtube.com/watch?v=UceaB4D0jpo')
	time.sleep(100)
	while True:
		question = input("Brauchst du noch ein kleines Warm-Up? ")
		if question.lower() == 'ja':
			print("Spiel")
			break
		elif question.lower() == 'nein':
			break
		else:
			print("Bitte schreibe entweder 'ja' oder 'nein'!\n")
			continue
	time.sleep(300)
	print("Zeit zum Weiterarbeiten!\n")
	repeats += 1

print("Ende!")