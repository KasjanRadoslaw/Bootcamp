# Frage nach dem Namen.
name = input("Wie heißt du? ")
print(f"{name.title()}, was ein toller Name!\n")

# Frage nach dem Alter mit Kommentar.
age = input("Wie alt bist du? ")
if int(age) < 20:
	print("Du bist noch ein Jugendlicher!\n")
else:
	print("Du bist schon erwachsen!\n")
	
# Frage mit 2 Antwortoptionen.
question = input("Magst du eigentlich Hunde mehr als Katzen? ")
if question.lower() == "ja":
	print("Ich auch!\n")
if question.lower() == "nein":
	print("Du bist also eher ein Katzenmensch!\n")
	
# Nach Namen Fragen.
prompt = "Hast du noch Fragen an mich?\n"
prompt += "Du kannst nach meinem Namen fragen. "
question2 = input(prompt)
if 'name' in question2.lower():
	print("Mein Name lautet Ada!")
else:
	print("\nVielen Dank für das Gespräch!")
