from .lcd import LCD

lcd = LCD()


def welcome(line_1_display, line_2_display):
    lcd.welcome(line_1_display, line_2_display)


def display(line_1_display, line_2_display):
    lcd.display(line_1_display, line_2_display)
