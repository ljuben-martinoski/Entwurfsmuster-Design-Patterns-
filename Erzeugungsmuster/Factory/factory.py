# Wir definieren die verschidenen Pizza-Typen
class SalamiPizza:
    def zubereiten(self):
        return "Salami-Pizza wird gebacken! "
    

class HawaiiPizza:
    def zubereiten(self):
        return "Hawaii-Pizza wird gebacken! "


# Die Factory(Die Fabrik)
class PizzaFactory:        
    @staticmethod
    def erstelle_pizza(typ):
        if typ == "Salami":
            return SalamiPizza()
        elif typ == "Hawaii":
            return HawaiiPizza()
        else:
            return "Diese Sorte haben wir nicht! "


# Nutzung durch der Anfänger (Der Kunde)
bestellung = "Hawaii"
"""# erstellen eine var. meine pizza,wo wir setzen die factory mit die funktion 
erstelle piza und bestellung als perimeter/argument."""
meine_pizza = PizzaFactory.erstelle_pizza(bestellung)

print(meine_pizza.zubereiten())  # 
"""wir rufen die meine pizza variable mit die zub. funktion"""
