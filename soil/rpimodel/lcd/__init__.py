from .lcd import LCD

lcd = LCD()


def display(*args, **kwargs):
    lcd.display(*args, **kwargs)
