let index = 0
basic.forever(function () {
    radio.sendString("我")
    basic.showIcon(IconNames.Heart)
    music.playMelody("- - - - - - - - ", 120)
    basic.showIcon(IconNames.Heart)
    music.playMelody("- - - - - - - - ", 120)
    basic.showString("Hello!")
    basic.clearScreen()
    radio.sendString("")
    led.plotBarGraph(
    0,
    0
    )
    music.playMelody("- - - - - - - - ", 120)
    led.enable(false)
    radio.sendValue("name", 0)
    index += 1
    basic.clearScreen()
})
basic.forever(function () {
    basic.showLeds(`
        . # # # .
        # . # . #
        # # # # .
        # # . # #
        # . . . .
        `)
    basic.showLeds(`
        . # # # .
        . . # . .
        # # # # #
        # # # # #
        # . . . #
        `)
    basic.showLeds(`
        . . # . .
        . # # # .
        . . # . .
        . . # . .
        . # # # .
        `)
    basic.showLeds(`
        . . . . #
        . . . # #
        . . # # #
        . # # # #
        # # # # #
        `)
})
