from settings import config


def aktiviere_dark_mode():
    config.theme = "Dark"
    print(f"Manager:Theme auf {config.theme} gesetzt. ")
    