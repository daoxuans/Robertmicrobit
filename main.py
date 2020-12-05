index = 0

def on_forever():
    global index
    radio.send_string("我")
    basic.show_icon(IconNames.HEART)
    music.play_melody("- - - - - - - - ", 120)
    basic.show_icon(IconNames.HEART)
    music.play_melody("- - - - - - - - ", 120)
    basic.show_string("Hello!")
    basic.clear_screen()
    radio.send_string("")
    led.plot_bar_graph(0, 0)
    music.play_melody("- - - - - - - - ", 120)
    led.enable(False)
    radio.send_value("name", 0)
    index += 1
    basic.clear_screen()
basic.forever(on_forever)

def on_forever2():
    basic.show_leds("""
        . # # # .
        # . # . #
        # # # # .
        # # . # #
        # . . . .
        """)
    basic.show_leds("""
        . # # # .
        . . # . .
        # # # # #
        # # # # #
        # . . . #
        """)
    basic.show_leds("""
        . . # . .
        . # # # .
        . . # . .
        . . # . .
        . # # # .
        """)
    basic.show_leds("""
        . . . . #
        . . . # #
        . . # # #
        . # # # #
        # # # # #
        """)
basic.forever(on_forever2)
