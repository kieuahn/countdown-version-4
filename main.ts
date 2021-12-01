input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    if (set_Timerhours <= 12) {
        basic.showNumber(set_Timerhours)
        set_Timerhours += 1
        basic.pause(100)
        basic.clearScreen()
    } else {
        set_Timerhours = 0
    }
    
})
input.onPinPressed(TouchPin.P2, function on_pin_pressed_p2() {
    music.playTone(262, music.beat(BeatFraction.Whole))
    basic.showString("" + ("" + hour) + ":" + ("" + min2) + ":" + ("" + second))
    basic.showString("" + ("" + input.temperature()))
    basic.showString("" + ("" + input.lightLevel()))
    basic.pause(1000)
})
input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
    
    if (set_Timerseconds < 59) {
        basic.showNumber(set_Timerseconds)
        set_Timerseconds += 1
    } else {
        set_Timerseconds = 0
    }
    
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    if (set_Timerminutes < 59) {
        basic.showNumber(set_Timerminutes)
        set_Timerminutes += 1
    } else {
        set_Timerminutes = 0
    }
    
})
input.onPinPressed(TouchPin.P1, function on_pin_pressed_p1() {
    
})
input.onGesture(Gesture.Shake, function on_gesture_shake() {
    
    while (set_Timerseconds > 0) {
        set_Timerseconds += 0 - 1
        music.playTone(262, music.beat(BeatFraction.Quarter))
        if (set_Timerseconds == 0) {
            set_Timerminutes += 0 - 1
            music.playTone(262, music.beat(BeatFraction.Quarter))
            set_Timerseconds = 59
            if (set_Timerminutes == 0) {
                set_Timerhours += 0 - 1
                music.playTone(262, music.beat(BeatFraction.Quarter))
                set_Timerminutes = 59
                basic.showString("" + ("" + set_Timerhours) + ":" + ("" + set_Timerminutes) + ":" + ("" + set_Timerseconds))
            }
            
            basic.showString("" + ("" + set_Timerminutes) + ":" + ("" + set_Timerseconds))
        }
        
        basic.showNumber(set_Timerseconds)
        basic.pause(100)
    }
})
let set_Timerseconds = 0
let second = 0
let min2 = 0
let hour = 0
let set_Timerminutes = 0
let set_Timerhours = 0
set_Timerhours = 0
set_Timerminutes = 0
hour = 12
min2 = 59
second = 50
basic.forever(function on_forever() {
    
    second += 1
    if (second >= 60) {
        second = 0
        min2 += 1
    }
    
    if (min2 >= 60) {
        min2 = 0
        hour += 1
    }
    
    if (hour >= 24) {
        hour = 0
    }
    
})
