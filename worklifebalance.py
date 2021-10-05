import webbrowser
import time

repeats = 0

while repeats < 5:
	time.sleep(5400)
	print("Zeit für eine Pause!")
	webbrowser.open('https://www.youtube.com/watch?v=UceaB4D0jpo')
	time.sleep(400)
	print("Zeit zum Weiterarbeiten!\n")
	repeats += 1

print("Ende!")