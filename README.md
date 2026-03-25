# Entwurfsmuster — Mein Lernprojekt 🧠

Hey! Das hier ist mein persönliches Projekt, in dem ich **Design Patterns** (auf Deutsch: Entwurfsmuster) lerne.

Design Patterns sind keine Bibliotheken oder Frameworks — es sind einfach **clevere Lösungsideen**, die schlaue Entwickler über die Jahre gesammelt haben. Statt jedes Problem neu zu erfinden, nutzt man ein bewährtes Muster.

Stell dir vor, du baust ein Haus. Du musst nicht selbst herausfinden, wie Treppen funktionieren — es gibt bereits einen Standard dafür. Genau das sind Design Patterns für Code.

---

## Was ich bisher gelernt habe

### 🏭 Erzeugungsmuster
*Diese Muster helfen dabei, Objekte zu erstellen — auf eine saubere und flexible Art.*

#### Singleton (`SIngeltonPatern/`)
> **Idee:** Es darf immer nur **ein einziges** Objekt dieser Klasse geben.

**Reales Beispiel:** Die App-Einstellungen. Es macht keinen Sinn, zwei verschiedene Einstellungs-Objekte zu haben — alle Teile des Programms sollen dieselben Einstellungen sehen.

| Datei | Was sie macht |
|---|---|
| `settings.py` | Erstellt das einzige `AppSettings`-Objekt und stellt es bereit |
| `manager.py` | Importiert das Objekt und kann es verändern (z.B. Dark Mode an) |
| `main.py` | Zeigt, dass alle denselben Stand sehen — egal wer es ändert |

```
Start: Light   ← settings.py hat Light gesetzt
Manager ändert auf Dark...
Ende:  Dark    ← main.py sieht die Änderung sofort!
```

---

#### Factory (`Factory/`)
> **Idee:** Du sagst nur WAS du willst — die Fabrik entscheidet WIE es gebaut wird.

**Reales Beispiel:** Eine Pizzeria. Du sagst "Hawaii" — der Koch weiß was zu tun ist. Du musst nicht selbst backen.

```python
meine_pizza = PizzaFactory.erstelle_pizza("Hawaii")
# Du fragst die Fabrik → sie gibt dir das fertige Objekt zurück
```

Datei: `factory.py`

---

### 🏛️ Strukturmuster
*Diese Muster helfen dabei, Klassen und Objekte sauber zu organisieren.*

#### Fassade (`Facade.py`)
> **Idee:** Viele komplizierte Klassen werden hinter **einer einfachen Klasse** versteckt.

**Reales Beispiel:** Eine Fernbedienung. Du drückst einen Knopf — im Hintergrund geht der Fernseher an, der Sound stellt sich ein, Netflix öffnet sich. Du siehst das alles nicht, du drückst nur einen Knopf.

```python
mein_kino = HeimkinoFassade()
mein_kino.film_abend_starten()
# Ein Befehl → alles läuft automatisch
```

Ohne Fassade müsstest du das selbst schreiben:
```python
tv = Fernseher()
sound = SoundSystem()
netflix = StreamingDienst()
tv.an()
sound.einstellen()
netflix.starten()
# Das ist viel zu umständlich!
```

---

## Ordnerstruktur

```
Entwurfsmuster/
│
├── Erzeugungsmuster/          ← Wie erstelle ich Objekte?
│   ├── SIngeltonPatern/       ← Nur ein Objekt erlaubt
│   │   ├── settings.py
│   │   ├── manager.py
│   │   └── main.py
│   │
│   └── Factory/               ← Die Fabrik baut für dich
│       └── factory.py
│
└── Strukturmuster/            ← Wie baue ich meinen Code auf?
    └── Facade.py              ← Eine einfache Oberfläche für Chaos
```

---

## Was ich dabei gelernt habe

- Was `self` bedeutet — es ist einfach das Objekt selbst
- Wie man Objekte in `__init__` mit `self.xyz` speichert
- Dass man Code in Module aufteilen kann und sie mit `import` verbindet
- Dass gute Muster Code lesbarer und wartbarer machen

---

*Projekt in Bearbeitung — es kommen noch mehr Muster dazu!*
