pocet = 1
y = 0

def hlavní():
    global pocet, y
    if pocet == 1:
        cislo = randint(1, 6)
    else:
        cislo = randint(1, 10)
    if y == 1:
        if input.is_gesture(Gesture.SHAKE):
            y = 0

            if cislo == 1:
                basic.show_leds("""
                    . . . . .
                    . . . . .
                    . . # . .
                    . . . . .
                    . . . . .
                """)
            elif cislo == 2:
                basic.show_leds("""
                    . . . . .
                    . # . . .
                    . . . . .
                    . . . # .
                    . . . . .
                """)
            elif cislo == 3:
                basic.show_leds("""
                    . . . . .
                    . # . . .
                    . . # . .
                    . . . # .
                    . . . . .
                """)
            elif cislo == 4:
                basic.show_leds("""
                    . . . . .
                    . # . # .
                    . . . . .
                    . # . # .
                    . . . . .
                """)
            elif cislo == 5:
                basic.show_leds("""
                    . . . . .
                    . # . # .
                    . . # . .
                    . # . # .
                    . . . . .
                """)
            elif cislo == 6:
                basic.show_leds("""
                    . # . # .
                    . . . . .
                    . # . # .
                    . . . . .
                    . # . # .
                """)
            elif cislo == 7:
                basic.show_leds("""
                    # . . . #
                    . . . . .
                    # . # . #
                    . . . . .
                    # . . . #
                """)
            elif cislo == 8:
                basic.show_leds("""
                    # . . . #
                    . . # . .
                    # . . . #
                    . . # . .
                    # . . . #
                """)
            elif cislo == 9:
                basic.show_leds("""
                    # . . . #
                    . . # . .
                    # . # . #
                    . . # . .
                    # . . . #
                """)
            elif cislo == 10:
                basic.show_leds("""
                    # . . . #
                    . . # . .
                    # # . # #
                    . . # . .
                    # . . . #
                """)
            for i in range(cislo):
                music.play_tone(Note.C, music.beat(2))
                music.rest(music.beat(3))
basic.forever(hlavní)

def zamek():
    global y
    if input.button_is_pressed(Button.A):
        basic.show_icon(IconNames.HAPPY)
        y = 1
basic.forever(zamek)

def steny():
    global pocet
    if input.logo_is_pressed():
        pocet *= -1
        basic.show_string("Steny")
        if pocet == 1:
            basic.show_number(6)
        else:
            basic.show_number(10)
basic.forever(steny)
