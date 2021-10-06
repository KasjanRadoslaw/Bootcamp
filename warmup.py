import webbrowser
import time
import random

repeats = 0

while repeats < 5:
	time.sleep(5400)
	print("Zeit für eine Pause!")
	webbrowser.open('https://www.youtube.com/watch?v=UceaB4D0jpo')
	time.sleep(100)
	while True:
		question = input("Brauchst du noch ein kleines Warm-Up? ")
		if question.lower() == 'ja':
			number = random.randint(1, 100)
			tries = 6
			print("Ich bin Käptn Hook! Du willst meinen Schatz?")
			print("Du kannst ihn haben! Errate meine Zahl, von 1-100!\n")
			while tries > 0:
				guess = input("Wie lautet deine Zahl? ")
				if int(guess) < number:
					print("Zu niedrig, du Landratte!\n")
					tries -= 1
				elif int(guess) > number:
					print("Zu hoch!\n")
					tries -= 1
				else:
					print("Da liegst du goldrichtig!")
					break
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