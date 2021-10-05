import webbrowser
import time

prompt = input("Gebe 'suche' ein, um Google zu öffnen. ")
if prompt.lower() == 'suche':
    print("Der Browser wird geöffnet...")
    time.sleep(2)
    webbrowser.open('https://www.google.com')