#!/usr/bin/python3
# -*- coding: utf-8 -*-

# from pygame_loop import *

freq_array_x = (2000, 1000,  600,  300,  200,  170)   # Werte für X-Achse
freq_array_y = (2000, 1000,  600,  300,  200,  170)   # Werte für Y-Achse
freq_array_z = (8000, 6000, 4000, 3000, 2500, 2000)   # Werte für Z-Achse
freq_array_r = ( 250,  250,  120,  80,   60,    40)   # Werte für R-Achse


class JoyStickInput:
    def __init__(self):
        self.left = 0
        self.right = 0
        self.up = 0
        self.down = 0
        self.left_flag = 0
        self.right_flag = 0
        self.mid_x_flag = 0
        self.up_flag = 0
        self.down_flag = 0
        self.mid_y_flag = 0
        self.button_0 = 0
        self.button_1 = 0
        self.button_2 = 0
        self.button_3 = 0
        self.button_4 = 0
        self.button_5 = 0
        self.button_6 = 0
        self.button_7 = 0
        self.button_8 = 0
        self.button_9 = 0
        self.button_10 = 0
        self.button_11 = 0
        self.button_0_down = False
        self.button_1_down = False
        self.button_2_down = False
        self.button_3_down = False
        self.button_4_down = False
        self.button_5_down = False
        self.button_6_down = False
        self.button_7_down = False
        self.button_8_down = False
        self.button_9_down = False
        self.button_10_down = False
        self.button_11_down = False
        self.button_0_up = False
        self.button_1_up = False
        self.button_2_up = False
        self.button_3_up = False
        self.button_4_up = False
        self.button_5_up = False
        self.button_6_up = False
        self.button_7_up = False
        self.button_8_up = False
        self.button_9_up = False
        self.button_10_up = False
        self.button_11_up = False
        self.key_0 = 0
        self.key_0_down = 0
        self.key_1 = 0
        self.key_1_down = 0
        self.key_2 = 0
        self.key_2_down = 0
        self.run_exit = 0
        self.debug = 192

    def go_left(self):
        if self.left == 1 and self.left_flag == 0:
            self.left_flag = 1
            return True
        if self.left == 0 and self.left_flag == 1:
            self.left_flag = 0
        return False

    def is_left(self):
        if self.left == 1:
            return True
        return False

    def go_right(self):
        if self.right == 1 and self.right_flag == 0:
            self.right_flag = 1
            return True
        if self.right == 0 and self.right_flag == 1:
            self.right_flag = 0
        return False

    def is_right(self):
        if self.right == 1:
            return True
        return False

    def go_x_mid(self):
        if self.left == 0 and self.right == 0 and self.mid_x_flag == 0:
            self.mid_x_flag = 1
            return True
        if (self.left == 1 or self.right == 1) and self.mid_x_flag == 1:
            self.mid_x_flag = 0
        return False

    def is_x_mid(self):
        if self.left == 0 and self.right == 0:
            return True
        return False

    def go_up(self):
        if self.up == 1 and self.up_flag == 0:
            self.up_flag = 1
            return True
        if self.up == 0 and self.up_flag == 1:
            self.up_flag = 0
        return False

    def is_up(self):
        if self.up == 1:
            return True
        return False

    def go_down(self):
        if self.down == 1 and self.down_flag == 0:
            self.down_flag = 1
            return True
        if self.down == 0 and self.down_flag == 1:
            self.down_flag = 0
        return False

    def is_down(self):
        if self.down == 1:
            return True
        return False

    def go_y_mid(self):
        if self.up == 0 and self.down == 0 and self.mid_y_flag == 0:
            self.mid_y_flag = 1
            return True
        if (self.up == 1 or self.down == 1) and self.mid_y_flag == 1:
            self.mid_y_flag = 0
        return False

    def is_y_mid(self):
        if self.up == 0 and self.down == 0:
            return True
        return False

    def set_button_0(self):
        self.button_0 = True

    def get_button_0(self):
        return self.button_0

    def set_button_1(self):
        self.button_1 = True

    def get_button_1(self):
        return self.button_1

    def set_button_2(self):
        self.button_2 = True

    def get_button_2(self):
        return self.button_2

    def set_button_3(self):
        self.button_3 = True

    def get_button_3(self):
        return self.button_3

    def set_button_4(self):
        self.button_4 = True

    def get_button_4(self):
        return self.button_4

    def set_button_5(self):
        self.button_5 = True

    def get_button_5(self):
        return self.button_5

    def set_button_6(self):
        self.button_6 = True

    def get_button_6(self):
        return self.button_6

    def set_button_7(self):
        self.button_7 = True

    def get_button_7(self):
        return self.button_7

    def is_button_0_pressed(self):
        if self.button_0 == 1 and self.button_0_down == 0:
            self.button_0_down = 1
            return True
        if self.button_0 == 0 and self.button_0_down == 1:
            self.button_0_down = 0
        return False

    def is_button_0_release(self):
        if self.button_0 == 0 and self.button_0_up == 0:
            self.button_0_up = 1
            return True
        if self.button_0 == 1 and self.button_0_up == 1:
            self.button_0_up = 0
        return False

    def is_button_1_pressed(self):
        if self.button_1 == 1 and self.button_1_down == 0:
            self.button_1_down = 1
            return True
        if self.button_1 == 0 and self.button_1_down == 1:
            self.button_1_down = 0
        return False

    def is_button_1_release(self):
        if self.button_1 == 0 and self.button_1_up == 0:
            self.button_1_up = 1
            return True
        if self.button_1 == 1 and self.button_1_up == 1:
            self.button_1_up = 0
        return False

    def is_button_2_pressed(self):
        if self.button_2 == 1 and self.button_2_down == 0:
            self.button_2_down = 1
            return True
        if self.button_2 == 0 and self.button_2_down == 1:
            self.button_2_down = 0
        return False

    def is_button_2_release(self):
        if self.button_2 == 0 and self.button_2_up == 0:
            self.button_2_up = 1
            return True
        if self.button_2 == 1 and self.button_2_up == 1:
            self.button_2_up = 0
        return False

    def is_button_3_pressed(self):
        if self.button_3 == 1 and self.button_3_down == 0:
            self.button_3_down = 1
            return True
        if self.button_3 == 0 and self.button_3_down == 1:
            self.button_3_down = 0
        return False

    def is_button_3_release(self):
        if self.button_3 == 0 and self.button_3_up == 0:
            self.button_3_up = 1
            return True
        if self.button_3 == 1 and self.button_3_up == 1:
            self.button_3_up = 0
        return False

    def is_button_4_pressed(self):
        if self.button_4 == 1 and self.button_4_down == 0:
            self.button_4_down = 1
            return True
        if self.button_4 == 0 and self.button_4_down == 1:
            self.button_4_down = 0
        return False

    def is_button_4_release(self):
        if self.button_4 == 0 and self.button_4_up == 0:
            self.button_4_up = 1
            return True
        if self.button_4 == 1 and self.button_4_up == 1:
            self.button_4_up = 0
        return False

    def is_button_5_pressed(self):
        if self.button_5 == 1 and self.button_5_down == 0:
            self.button_5_down = 1
            return True
        if self.button_5 == 0 and self.button_5_down == 1:
            self.button_5_down = 0
        return False

    def is_button_5_release(self):
        if self.button_5 == 0 and self.button_5_up == 0:
            self.button_5_up = 1
            return True
        if self.button_5 == 1 and self.button_5_up == 1:
            self.button_5_up = 0
        return False

    def is_button_6_pressed(self):
        if self.button_6 == 1 and self.button_6_down == 0:
            self.button_6_down = 1
            return True
        if self.button_6 == 0 and self.button_6_down == 1:
            self.button_6_down = 0
        return False

    def is_button_6_release(self):
        if self.button_6 == 0 and self.button_6_up == 0:
            self.button_6_up = 1
            return True
        if self.button_6 == 1 and self.button_6_up == 1:
            self.button_6_up = 0
        return False

    def is_button_7_pressed(self):
        if self.button_7 == 1 and self.button_7_down == 0:
            self.button_7_down = 1
            return True
        if self.button_7 == 0 and self.button_7_down == 1:
            self.button_7_down = 0
        return False

    def is_button_7_release(self):
        if self.button_7 == 0 and self.button_7_up == 0:
            self.button_7_up = 1
            return True
        if self.button_7 == 1 and self.button_7_up == 1:
            self.button_7_up = 0
        return False

    def is_key_0_pressed(self):
        if self.key_0 == 1 and self.key_0_down == 0:
            self.key_0_down = 1
            return True
        if self.key_0 == 0 and self.key_0_down == 1:
            self.key_0_down = 0
        return False

    def is_key_1_pressed(self):
        if self.key_1 == 1 and self.key_1_down == 0:
            self.key_1_down = 1
            return True
        if self.key_1 == 0 and self.key_1_down == 1:
            self.key_1_down = 0
        return False

    def is_key_2_pressed(self):
        if self.key_2 == 1 and self.key_2_down == 0:
            self.key_2_down = 1
            return True
        if self.key_2 == 0 and self.key_2_down == 1:
            self.key_2_down = 0
        return False

    def printout(self):
        return "{0} {1} {2} {3} {4} {5} {6} {7} {8} {9} {10} {11}".format(self.left, self.right, self.up, self.down, self.button_0, self.button_1, self.button_2, self.button_3, self.button_4, self.button_5, self.button_6, self.button_7)


class UBootObj:
    def __init__(self):
        self.speed_x_act = 0
        self.speed_x_stop = 0
        self.speed_x_max = 5
        self.speed_y_act = 0
        self.speed_y_stop = 0
        self.speed_y_max = 5
        self.speed_z1_act = 0
        self.speed_z1_stop = 0
        self.speed_z1_max = 5
        self.speed_z2_act = 0
        self.speed_z2_stop = 0
        self.speed_z2_max = 5
        self.speed_r_act = 0
        self.speed_r_stop = 0
        self.speed_r_max = 5

    def reset_value(self):
        self.speed_x_act = 0
        self.speed_y_act = 0
        self.speed_z1_act = 0
        self.speed_z2_act = 0
        self.speed_r_act = 0
        self.speed_x_stop = 0
        self.speed_y_stop = 0
        self.speed_z1_stop = 0
        self.speed_z2_stop = 0
        self.speed_r_stop = 0

    def x_speed_inc(self):
        if self.speed_x_act < self.speed_x_max:
            self.speed_x_act += 1
            self.speed_x_stop = 0
            return True
        return False

    def x_speed_dec(self):
        if self.speed_x_act > 0:
            self.speed_x_act -= 1
            self.speed_x_stop = 0
            return True
        return False

    def x_speed_stop(self):
        if self.speed_x_act == 0 and self.speed_x_stop == 0:
            self.speed_x_stop = 1
            return True
        return False

    def get_x_speed_pwm(self):
        return freq_array_x[self.speed_x_act]

    def get_x_speed_act(self):
        return self.speed_x_act

    def y_speed_inc(self):
        if self.speed_y_act < self.speed_y_max:
            self.speed_y_act += 1
            self.speed_y_stop = 0
            return True
        return False

    def y_speed_dec(self):
        if self.speed_y_act > 0:
            self.speed_y_act -= 1
            self.speed_y_stop = 0
            return True
        return False

    def y_speed_stop(self):
        if self.speed_y_act == 0 and self.speed_y_stop == 0:
            self.speed_y_stop = 1
            return True
        return False

    def get_y_speed_pwm(self):
        return freq_array_y[self.speed_y_act]

    def get_y_speed_act(self):
        return self.speed_y_act

    def z1_speed_inc(self):
        if self.speed_z1_act < self.speed_z1_max:
            self.speed_z1_act += 1
            self.speed_z1_stop = 0
            return True
        return False

    def z1_speed_dec(self):
        if self.speed_z1_act > 0:
            self.speed_z1_act -= 1
            self.speed_z1_stop = 0
            return True
        return False

    def z1_speed_stop(self):
        if self.speed_z1_act == 0 and self.speed_z1_stop == 0:
            self.speed_z1_stop = 1
            return True
        return False

    def get_z1_speed_pwm(self):
        return freq_array_z[self.speed_z1_act]

    def get_z1_speed_act(self):
        return self.speed_z1_act

    def z2_speed_inc(self):
        if self.speed_z2_act < self.speed_z2_max:
            self.speed_z2_act += 1
            self.speed_z2_stop = 0
            return True
        return False

    def z2_speed_dec(self):
        if self.speed_z2_act > 0:
            self.speed_z2_act -= 1
            self.speed_z2_stop = 0
            return True
        return False

    def z2_speed_stop(self):
        if self.speed_z2_act == 0 and self.speed_z2_stop == 0:
            self.speed_z2_stop = 1
            return True
        return False

    def get_z2_speed_pwm(self):
        return freq_array_z[self.speed_z2_act]

    def get_z2_speed_act(self):
        return self.speed_z2_act

    def r_speed_inc(self):
        if self.speed_r_act < self.speed_r_max:
            self.speed_r_act += 1
            self.speed_r_stop = 0
            return True
        return False

    def r_speed_dec(self):
        if self.speed_r_act > 0:
            self.speed_r_act -= 1
            self.speed_r_stop = 0
            return True
        return False

    def r_speed_stop(self):
        if self.speed_r_act == 0 and self.speed_r_stop == 0:
            self.speed_r_stop = 1
            return True
        return False

    def get_r_speed_pwm(self):
        return freq_array_r[self.speed_r_act]

    def get_r_speed_act(self):
        return self.speed_r_act


class PositionObj:

    def __init__(self):
        self.pos_x = 0
        self.pos_y = 0
        self.pos_z1 = 0
        self.pos_z2 = 0
        self.pos_r = 0
        self.status = 0

    def get_x(self):
        return self.pos_x

    def get_y(self):
        return self.pos_y

    def get_z1(self):
        return self.pos_z1

    def get_z2(self):
        return self.pos_z2

    def get_r(self):
        return self.pos_r

    def pos_x_inc(self):
        self.pos_x += 1

    def pos_x_dec(self):
        self.pos_x -= 1

    def pos_y_inc(self):
        self.pos_y += 1

    def pos_y_dec(self):
        self.pos_y -= 1

    def pos_z1_inc(self):
        self.pos_z1 += 1

    def pos_z1_dec(self):
        self.pos_z1 -= 1

    def pos_z2_inc(self):
        self.pos_z2 += 1

    def pos_z2_dec(self):
        self.pos_z2 -= 1

    def pos_r_inc(self):
        self.pos_r += 1

    def pos_r_dec(self):
        self.pos_r -= 1

    def printout(self):
        return "X={0} Y={1} Z1={2} Z2={3} R={4} Status={5}".format(self.pos_x, self.pos_y, self.pos_z1, self.pos_z2, self.pos_r, self.status)


class ExtButton:
    def __init__(self):
        self.state_act = False
        self.state_down = False
        self.state_up = False

    def set_state(self, value):
        if value > 0:
            self.state_act = False
        else:
            self.state_act = True

    def get_state(self):
        return self.state_act

    def is_pressed(self):
        if self.state_act and not self.state_down:
            self.state_down = True
            return True
        if not self.state_act and self.state_down:
            self.state_down = False
        return False

    def is_release(self):
        if not self.state_act and not self.state_up:
            self.state_up = True
            return True
        if self.state_act and self.state_up:
            self.state_up = False
        return False


class PositionValid:
    def __init__(self):
        self.valid_x = False
        self.valid_y = False
        self.valid_z1 = False
        self.valid_z2 = False
        self.valid_r = False
        self.pos_okay = False

    def reset(self):
        self.valid_x = False
        self.valid_y = False
        self.valid_z1 = False
        self.valid_z2 = False
        self.valid_r = False

    def set_valid_x(self, value):
        self.valid_x = value
    
    def get_valid_x(self):
        return self.valid_x

    def set_valid_y(self, value):
        self.valid_y = value

    def get_valid_y(self):
        return self.valid_y

    def set_valid_z1(self, value):
        self.valid_z1 = value

    def get_valid_z1(self):
        return self.valid_z1

    def set_valid_z2(self, value):
        self.valid_z2 = value

    def get_valid_z2(self):
        return self.valid_z2

    def set_valid_r(self, value):
        self.valid_r = value

    def get_valid_r(self):
        return self.valid_r

    def is_pos_okay(self):
        if self.valid_x and self.valid_y and self.valid_z1 and self.valid_z2 and self.valid_r:
            return True
        return False


def x_skalieren(inkremente):
    return int(round((1024 / 49246) * inkremente))


def y_skalieren(inkremente):
    return int(round((768 / 34667) * inkremente))


def z_skalieren(inkremente):
    return int(round((1000 / 10000) * inkremente))


def r_skalieren(inkremente):
    return int(round((360 / 12800) * inkremente)) % 360


def clamp(x, minimum, maximum):
    return max(minimum, min(x, maximum))


def joystick_loopback():
    global position_uboot
    global position_stepper
    global joystickinput

    if joystickinput.left == 1:
        position_uboot.pos_x = position_uboot.pos_x + 1
    if joystickinput.right == 1:
        position_uboot.pos_x = position_uboot.pos_x - 1
    if joystickinput.up == 1:
        position_uboot.pos_y = position_uboot.pos_y + 1
    if joystickinput.down == 1:
        position_uboot.pos_y = position_uboot.pos_y - 1
    if joystickinput.button_0 == 1:
        position_uboot.pos_z1 = position_uboot.pos_z1 + 1
    if joystickinput.button_1 == 1:
        position_uboot.pos_z1 = position_uboot.pos_z1 - 1
    if joystickinput.button_2 == 1:
        position_uboot.pos_z2 = position_uboot.pos_z2 + 1
    if joystickinput.button_3 == 1:
        position_uboot.pos_z2 = position_uboot.pos_z2 - 1
    if joystickinput.button_5 == 1:
        position_uboot.pos_r = position_uboot.pos_r + 1
    if joystickinput.button_7 == 1:
        position_uboot.pos_r = position_uboot.pos_r - 1


# ----------------------------------------------------------------------------------------------------------------------
def main():
    global joystickinput
    global position_stepper
    global position_uboot
    global ext_button_start, ext_button_stop
    #global speed_uboot
    #global task_timer

    joystickinput = JoyStickInput()

    position_stepper = PositionObj()
    position_uboot = PositionObj()

    uboot = UBootObj()

    ext_button_start = ExtButton()
    ext_button_stop = ExtButton()

    if True:
        print("X-Inc")
        for x in range(0, uboot.speed_x_max + 1):
            print(uboot.get_x_speed_pwm())
            uboot.x_speed_inc()
        print("X-Dec")
        for x in range(0, uboot.speed_x_max + 1):
            print(uboot.get_x_speed_pwm())
            uboot.x_speed_dec()

    if True:
        print("Y-Inc")
        for x in range(0, uboot.speed_y_max + 1):
            print(uboot.get_y_speed_pwm())
            uboot.y_speed_inc()
        print("Y-Dec")
        for x in range(0, uboot.speed_y_max + 1):
            print(uboot.get_y_speed_pwm())
            uboot.y_speed_dec()

    if True:
        print("Z1-Inc")
        for x in range(0, uboot.speed_z1_max + 1):
            print(uboot.get_z1_speed_pwm())
            uboot.z1_speed_inc()
        print("Z1-Dec")
        for x in range(0, uboot.speed_z1_max + 1):
            print(uboot.get_z1_speed_pwm())
            uboot.z1_speed_dec()

    if True:
        print("Z2-Inc")
        for x in range(0, uboot.speed_z2_max + 1):
            print(uboot.get_z2_speed_pwm())
            uboot.z2_speed_inc()
        print("Z2-Dec")
        for x in range(0, uboot.speed_z2_max + 1):
            print(uboot.get_z2_speed_pwm())
            uboot.z2_speed_dec()

    if True:
        print("R-Inc")
        for x in range(0, uboot.speed_r_max + 1):
            print(uboot.get_r_speed_pwm())
            uboot.r_speed_inc()
        print("R-Dec")
        for x in range(0, uboot.speed_r_max + 1):
            print(uboot.get_r_speed_pwm())
            uboot.r_speed_dec()

    ext_button_start.set_state(1)
    print(ext_button_start.is_pressed())
    print(ext_button_start.is_pressed())
    ext_button_start.set_state(0)
    print(ext_button_start.is_pressed())
    print(ext_button_start.is_release())
    print(ext_button_start.is_release())



if __name__ == "__main__":
    main()
