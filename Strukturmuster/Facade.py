# ============================================================
# ENTWURFSMUSTER: FASSADE (Facade Pattern)
# ============================================================
# Idee: Statt viele komplizierte Klassen einzeln zu bedienen,
# gibt es EINE einfache Klasse, die alles für dich erledigt.
# So wie eine Fernbedienung: Du drückst einen Knopf,
# und im Hintergrund passiert ganz viel automatisch.
# ============================================================


# --- Die Subsysteme (das "Chaos" im Hintergrund) ---
# Diese drei Klassen sind die echten Geräte.
# Jede kann nur ihre eine Aufgabe.

class Fernseher:
    def an(self):
        # Schaltet den Fernseher ein
        print("Fernseher: Geht an...")


class SoundSystem:
    def einstellen(self):
        # Stellt den Surround-Sound ein
        print("Sound: Surround-Sound aktiviert.")


class StreamingDienst:
    def starten(self):
        # Öffnet die Streaming-App
        print("Netflix: App wird geladen...")


# --- Die Fassade (die einfache Lösung) ---
# Diese Klasse kennt alle drei Geräte oben.
# Sie fasst alles in EINER einzigen Methode zusammen,
# damit der Benutzer sich um nichts kümmern muss.

class HeimkinoFassade:

    def __init__(self):
        # Beim Erstellen der Fassade werden alle Geräte vorbereitet
        self.tv = Fernseher()
        self.sound = SoundSystem()
        self.netflix = StreamingDienst()

    def film_abend_starten(self):
        # Ein einziger Aufruf startet ALLES in der richtigen Reihenfolge:
        # 1. Fernseher an
        # 2. Sound einstellen
        # 3. Netflix starten
        print("--- Vorbereitung für den Film läuft ---")
        self.tv.an()
        self.sound.einstellen()
        self.netflix.starten()
        print("--- Viel Spaß beim Schauen! ---")


# Ohne Fassade müsstest du hier 3-5 Zeilen Code schreiben.
# Mit Fassade ist es nur ein einziger Befehl:

mein_kino = HeimkinoFassade()
mein_kino.film_abend_starten()