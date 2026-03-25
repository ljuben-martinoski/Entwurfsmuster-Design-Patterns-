#   Das Model(Daten und Logic)
# erstellen klass model mit constructor init
class Model:
    def __init__(self):
        self.data = "Hello World"  # initializing a variable mit der name .data

    def set_data(self, value):
        self.data = value

    def get_data(self):
        return self.data 


# Die View 
#  erstellen class View 
class View:
    # erstellen method display_message mit parameter message
    def display_message(self, message):
        print(f"Anzeige: {message}") 
# erstellen ein method get_user_input das habe 
# kine parameter und nehmt input vom Benutzer. 

    def get_user_input(self):
        return input("Gib einen neuen Text ein: ")
    

# Der Controller(Das Gehirn)
class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def update_view(self):
        # holt daten aus dem MOdel und gibt sie an die View
        data = self.model.get_data()
        self.view.display_message(data)

    def change_data(self):
        # holt eingabe von der View und speichert sie im Model
        new_value = self.view.get_user_input()
        self.model.set_data(new_value)    


# Das Program starten
# Initialisierung
my_model = Model()
my_view = View()
my_controller = Controller(my_model, my_view)

# 1. Zeige Standard-Daten
my_controller.update_view()

# 2. Ändere Daten über den Controller
my_controller.change_data()

# 3. Zeige aktualisierte Daten
my_controller.update_view()



