import random
number = random.randint(1, 100)
tries = 0
won = False
print("Ich bin Käptn Hook! Du willst meinen Schatz?")
print("Du kannst ihn haben! Errate meine Zahl, von 1-100!\n")
while won == False:
	guess = input("Wie lautet deine Zahl? ")
	if int(guess) < number:
		print("Zu niedrig, du Landratte!\n")
		tries += 1
	elif int(guess) > number:
		print("Zu hoch!\n")
		tries += 1
	else:
		print("Da liegst du goldrichtig!")
		won = True
	if tries >= 6:
		break

if won == False:
	print("Game over!")
if won == True:
	print("Du kriegst meinen Schatz!")