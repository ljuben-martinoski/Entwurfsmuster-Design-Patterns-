"""das Observer-Pattern (Beobachter-Muster) ist ein echter Klassiker. 

Stell dir vor, du abonnierst einen YouTube-Kanal: 
Der Kanal (das Subjekt) weiß nicht, was du gerade machst, 
aber sobald ein neues Video kommt, 
schickt er eine Benachrichtigung an alle Abonnenten (die Observer)."""


# Das Grundgerüst
# Wir brauchen zwei Rollen: 
# Denjenigen, der die Nachrichten verschickt, und diejenigen, die zuhören.

# Die Klasse, die beobachtet wird (z.B. ein News-Kanal)
class NewsKanal:
    def __init__(self):
        self._abonnenten = []  # Leere Liste, in der wir die Abo.speichern

    def abo_hinzufugen(self, user):
        self._abonnenten.append(user)

    def sende_news(self, nachricht):
        print(f"Sende Nachricht: '{nachricht}'....")
        for user in self._abonnenten:
            user.update(nachricht)

# Die Klasse, die reagiert auf Nachrichten(der Beobachter)
# (z.B. ein Nutzer) 


class User:
    # Konstruktor der Klasse User
    def __init__(self, name):
        self.name = name
    # Methode, die aufgerufen wird, wenn eine Nachricht kommt

    def update(self, nachricht):
        print(f"{self.name} hat die Nachricht '{nachricht}' gelesen.") 


# So benutzen wir das Observer-Pattern


mein_kanal = NewsKanal()
alice = User("Alice")
bob = User("Bob")

mein_kanal.abo_hinzufugen(alice)
mein_kanal.abo_hinzufugen(bob)

mein_kanal.sende_news("Neues Video: Die Welt von Python!")