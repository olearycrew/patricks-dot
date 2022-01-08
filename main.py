def on_button_pressed_a():
    PSO()
    basic.show_string("Jump")
    basic.clear_screen()
    RUN()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    PSO()
    basic.show_string("Wave")
    basic.show_icon(IconNames.GIRAFFE)
    basic.show_leds("""
        # # . . .
                . # . . .
                # # . . .
                . # # # .
                . . . # .
    """)
    basic.show_icon(IconNames.GIRAFFE)
    basic.show_leds("""
        . # # . .
                . . # . .
                . . # . .
                # . # # #
                # . # . #
    """)
    basic.show_leds("""
        . . # # .
                . . . # .
                . . . # .
                # # . # #
                # # . # .
    """)
    basic.show_leds("""
        . . # . .
                . # . # .
                . . . # .
                # # . # #
                # # . # .
    """)
    basic.show_leds("""
        . . . . .
                . # # . .
                . # . # .
                # # . # #
                # # . # .
    """)
    basic.show_leds("""
        . . # . .
                . # . # .
                . . . # .
                # # . # #
                # # . # .
    """)
    basic.show_leds("""
        . . # # .
                . . . # .
                . . . # .
                # # . # #
                # # . # .
    """)
    basic.show_leds("""
        . . # # .
                . . . # .
                . . # # .
                # # . # #
                # # . . .
    """)
    basic.show_leds("""
        . . # # .
                . . . # .
                . . . # .
                # # . # #
                # # . # .
    """)
    basic.show_icon(IconNames.HEART)
    basic.clear_screen()
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    PSO()
    basic.show_string("Shell")
    basic.show_icon(IconNames.TORTOISE)
    basic.show_leds("""
        . . . . .
                . # # # .
                # # # # .
                . # . # .
                . . . . .
    """)
    basic.show_leds("""
        . . . . .
                . # # # .
                # # # # .
                . . . . .
                . . . . .
    """)
    basic.show_leds("""
        . . . . .
                . # # # .
                . # # # .
                . . . . .
                . . . . .
    """)
    basic.show_leds("""
        . . . . .
                . . . . .
                . # # # .
                . # # # .
                . . . . .
    """)
    basic.show_leds("""
        . . . . .
                . . . . .
                . . . . .
                . # # # .
                . # # # .
    """)
    basic.clear_screen()
    basic.show_icon(IconNames.HEART)
input.on_button_pressed(Button.B, on_button_pressed_b)

def PSO():
    basic.show_leds("""
        . . . . .
                . . . . .
                . . # . .
                . . . . .
                . . . . .
    """)
    basic.show_leds("""
        . . . . .
                . . # . .
                . # . # .
                . . # . .
                . . . . .
    """)
    basic.show_leds("""
        . . # . .
                . # . # .
                # . . . #
                . # . # .
                . . # . .
    """)
    basic.show_leds("""
        . # . # .
                # . . . #
                . . . . .
                # . . . #
                . # . # .
    """)
    basic.show_leds("""
        # . . . #
                . . . . .
                . . . . .
                . . . . .
                # . . . #
    """)
    basic.clear_screen()
def RUN():
    basic.show_icon(IconNames.STICK_FIGURE)
    basic.show_leds("""
        # . # . #
                . # # # .
                . . # . .
                . . # . .
                . # . # .
    """)
    basic.show_icon(IconNames.STICK_FIGURE)
    basic.show_leds("""
        . . # . .
                . # # # .
                # . # . #
                . . # . .
                . # . # .
    """)
    basic.show_icon(IconNames.STICK_FIGURE)
    basic.clear_screen()
    basic.show_icon(IconNames.HEART)

def on_forever():
    pass
basic.forever(on_forever)
