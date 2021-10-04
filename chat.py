name = input("Wie heißt du? ")
print(f"{name.title()}, was ein toller Name!\n")
age = input("Wie alt bist du? ")
if int(age) < 20:
	print("Du bist noch ein Jugendlicher!\n")
else:
	print("Du bist schon erwachsen!\n")
question = input("Magst du eigentlich Hunde mehr als Katzen? ")
if question.lower() == "ja":
	print("Ich auch!\n")
if question.lower() == "nein":
	print("Du bist also eher ein Katzenmensch!\n")
prompt = "Hast du noch Fragen an mich?"
prompt += "\nTippe 'name', um den Namen zu erfahren."
prompt += "\nSchreibe was anderes, um das Gespräch zu beenden. "
question2 = input(prompt)
if question2.lower() == 'name':
	print("Mein Name lautet Ada!")
else:
	print("\nVielen Dank für das Gespräch!")

