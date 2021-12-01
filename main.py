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

def on_pin_pressed_p2():
    music.play_tone(262, music.beat(BeatFraction.WHOLE))
    basic.show_string("" + str(hour) + ":" + str(min2) + ":" + str(second))
    basic.show_string("" + str((input.temperature())))
    basic.show_string("" + str((input.light_level())))
    basic.pause(1000)
input.on_pin_pressed(TouchPin.P2, on_pin_pressed_p2)

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

def on_pin_pressed_p1():
    pass
input.on_pin_pressed(TouchPin.P1, on_pin_pressed_p1)

def on_gesture_shake():
    global set_Timerseconds, set_Timerminutes, set_Timerhours
    while set_Timerseconds > 0:
        set_Timerseconds += 0 - 1
        music.play_tone(262, music.beat(BeatFraction.QUARTER))
        if set_Timerseconds == 0:
            set_Timerminutes += 0 - 1
            music.play_tone(262, music.beat(BeatFraction.QUARTER))
            set_Timerseconds = 59
            if set_Timerminutes == 0:
                set_Timerhours += 0 - 1
                music.play_tone(262, music.beat(BeatFraction.QUARTER))
                set_Timerminutes = 59
                basic.show_string("" + str(set_Timerhours) + ":" + str(set_Timerminutes) + ":" + str(set_Timerseconds))
            basic.show_string("" + str(set_Timerminutes) + ":" + str(set_Timerseconds))
        basic.show_number(set_Timerseconds)
        basic.pause(100)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

set_Timerseconds = 0
second = 0
min2 = 0
hour = 0
set_Timerminutes = 0
set_Timerhours = 0
set_Timerhours = 0
set_Timerminutes = 0
hour = 12
min2 = 59
second = 50

def on_forever():
    global second, min2, hour
    second += 1
    if second >= 60:
        second = 0
        min2 += 1
    if min2 >= 60:
        min2 = 0
        hour += 1
    if hour >= 24:
        hour = 0
basic.forever(on_forever)
