def on_pin_pressed_p0():
    global set_Timerminutes
    if set_Timerminutes < 59:
        basic.show_number(set_Timerminutes)
        set_Timerminutes += 10
    else:
        set_Timerminutes = 0
input.on_pin_pressed(TouchPin.P0, on_pin_pressed_p0)

def on_button_pressed_a():
    global set_Timerhours
    if set_Timerhours <= 12:
        basic.show_number(set_Timerhours)
        set_Timerhours += 1
        basic.pause(100)
        basic.clear_screen()
    else:
        set_Timerhours = 0
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global set_Timerseconds
    if set_Timerseconds < 59:
        basic.show_number(set_Timerseconds)
        set_Timerseconds += 1
    else:
        set_Timerseconds = 0
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global set_Timerminutes
    if set_Timerminutes < 59:
        basic.show_number(set_Timerminutes)
        set_Timerminutes += 1
    else:
        set_Timerminutes = 0
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    global set_Timerseconds, set_Timerminutes, set_Timerhours
    while set_Timerseconds > 0:
        set_Timerseconds += 0 - 1
        if set_Timerseconds == 0:
            set_Timerminutes += 0 - 1
            set_Timerseconds = 59
            if set_Timerminutes == 0:
                set_Timerhours += 0 - 1
                set_Timerminutes = 59
                basic.show_string("" + str(set_Timerhours) + ":" + str(set_Timerminutes) + ":" + str(set_Timerseconds))
            basic.show_string("" + str(set_Timerminutes) + ":" + str(set_Timerseconds))
        basic.show_number(set_Timerseconds)
        basic.pause(100)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

set_Timerseconds = 0
set_Timerminutes = 0
set_Timerhours = 0
set_Timerhours = 0
set_Timerminutes = 0

def on_forever():
    pass
basic.forever(on_forever)
