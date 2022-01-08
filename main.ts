input.onButtonPressed(Button.A, function () {
    PSO()
    basic.showString("Jump")
    basic.clearScreen()
    RUN()
})
input.onButtonPressed(Button.AB, function () {
    PSO()
    basic.showString("Wave")
    basic.showIcon(IconNames.Giraffe)
    basic.showLeds(`
        # # . . .
        . # . . .
        # # . . .
        . # # # .
        . . . # .
        `)
    basic.showIcon(IconNames.Giraffe)
    basic.showLeds(`
        . # # . .
        . . # . .
        . . # . .
        # . # # #
        # . # . #
        `)
    basic.showLeds(`
        . . # # .
        . . . # .
        . . . # .
        # # . # #
        # # . # .
        `)
    basic.showLeds(`
        . . # . .
        . # . # .
        . . . # .
        # # . # #
        # # . # .
        `)
    basic.showLeds(`
        . . . . .
        . # # . .
        . # . # .
        # # . # #
        # # . # .
        `)
    basic.showLeds(`
        . . # . .
        . # . # .
        . . . # .
        # # . # #
        # # . # .
        `)
    basic.showLeds(`
        . . # # .
        . . . # .
        . . . # .
        # # . # #
        # # . # .
        `)
    basic.showLeds(`
        . . # # .
        . . . # .
        . . # # .
        # # . # #
        # # . . .
        `)
    basic.showLeds(`
        . . # # .
        . . . # .
        . . . # .
        # # . # #
        # # . # .
        `)
    basic.showIcon(IconNames.Heart)
    basic.clearScreen()
})
input.onButtonPressed(Button.B, function () {
    PSO()
    basic.showString("Shell")
    basic.showIcon(IconNames.Tortoise)
    basic.showLeds(`
        . . . . .
        . # # # .
        # # # # .
        . # . # .
        . . . . .
        `)
    basic.showLeds(`
        . . . . .
        . # # # .
        # # # # .
        . . . . .
        . . . . .
        `)
    basic.showLeds(`
        . . . . .
        . # # # .
        . # # # .
        . . . . .
        . . . . .
        `)
    basic.showLeds(`
        . . . . .
        . . . . .
        . # # # .
        . # # # .
        . . . . .
        `)
    basic.showLeds(`
        . . . . .
        . . . . .
        . . . . .
        . # # # .
        . # # # .
        `)
    basic.clearScreen()
    basic.showIcon(IconNames.Heart)
})
function PSO () {
    basic.showLeds(`
        . . . . .
        . . . . .
        . . # . .
        . . . . .
        . . . . .
        `)
    basic.showLeds(`
        . . . . .
        . . # . .
        . # . # .
        . . # . .
        . . . . .
        `)
    basic.showLeds(`
        . . # . .
        . # . # .
        # . . . #
        . # . # .
        . . # . .
        `)
    basic.showLeds(`
        . # . # .
        # . . . #
        . . . . .
        # . . . #
        . # . # .
        `)
    basic.showLeds(`
        # . . . #
        . . . . .
        . . . . .
        . . . . .
        # . . . #
        `)
    basic.clearScreen()
}
function RUN () {
    basic.showIcon(IconNames.StickFigure)
    basic.showLeds(`
        # . # . #
        . # # # .
        . . # . .
        . . # . .
        . # . # .
        `)
    basic.showIcon(IconNames.StickFigure)
    basic.showLeds(`
        . . # . .
        . # # # .
        # . # . #
        . . # . .
        . # . # .
        `)
    basic.showIcon(IconNames.StickFigure)
    basic.clearScreen()
    basic.showIcon(IconNames.Heart)
}
basic.forever(function () {
	
})
