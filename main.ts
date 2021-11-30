input.onButtonPressed(Button.A, function () {
    if (set_Timerhours <= 12) {
        basic.showNumber(set_Timerhours)
        set_Timerhours += 1
        basic.pause(100)
        basic.clearScreen()
    } else {
        set_Timerhours = 0
    }
})
input.onButtonPressed(Button.AB, function () {
    if (set_Timerseconds < 59) {
        basic.showNumber(set_Timerseconds)
        set_Timerseconds += 1
    } else {
        set_Timerseconds = 0
    }
})
input.onButtonPressed(Button.B, function () {
    if (set_Timerminutes < 59) {
        basic.showNumber(set_Timerminutes)
        set_Timerminutes += 1
    } else {
        set_Timerminutes = 0
    }
})
input.onGesture(Gesture.Shake, function () {
    while (set_Timerseconds > 0) {
        set_Timerseconds += 0 - 1
        basic.showNumber(set_Timerseconds)
        basic.pause(100)
        basic.showString("" + set_Timerminutes + ":" + set_Timerseconds)
        if (set_Timerseconds == 0) {
            set_Timerminutes += 0 - 1
            set_Timerseconds = 59
            basic.showString("" + set_Timerminutes + ":" + set_Timerseconds)
            if (set_Timerminutes == 0) {
                set_Timerhours += 0 - 1
                set_Timerminutes = 59
                basic.showString("" + set_Timerhours + ":" + set_Timerminutes + ":" + set_Timerseconds)
            }
        }
    }
})
let set_Timerseconds = 0
let set_Timerminutes = 0
let set_Timerhours = 0
set_Timerhours = 0
set_Timerminutes = 0
basic.forever(function () {
	
})
