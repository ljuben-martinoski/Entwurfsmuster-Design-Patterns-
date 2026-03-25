import settings  # importieren das Objekt
import manager   # importiere die Funktion, die es ändert

print(f" Start: {settings.config.theme}")  # Ausgabe : Light
manager.aktiviere_dark_mode()   # Hier wird das  globale Objekt geändert
print(f"Ende: {settings.config.theme}")  # Ausgabe: Dark Theme


