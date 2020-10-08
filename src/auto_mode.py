#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Set-Points
set_points_x        = [ 796, 964]
set_points_y        = [ 375, 752]
set_points_z1       = [  83,  54]
set_points_z2       = [  83,  54]
set_points_r        = [   0, 270]
set_points_t        = [   1,   0]

pos_diff_x = 3
pos_diff_y = 3
pos_diff_z = 3
pos_diff_r = 3


# Referenzposition
# 1068 / 782 / 200 / 200 / 0

# Save Position
# 796 / 375 / 83 / 83 / 122

def Set_Point_Start():
    # Startposition:
    # 964 / 752 / 54 / 56 / 270
    global set_points_x, set_points_y, set_points_z1, set_points_z2, set_points_r, set_points_t

    set_points_x    = [796, 979]
    set_points_y    = [375, 774]
    set_points_z1   = [ 83,  47]
    set_points_z2   = [ 83,  47]
    set_points_r    = [ 90,  90]
    set_points_t    = [  1,   1]


def Set_Point_Mine_Crystals():
    # Mine Crystals
    # 885 / 539 / 182 / 174 / 245
    global set_points_x, set_points_y, set_points_z1, set_points_z2, set_points_r, set_points_t

    set_points_x    = [796, 885]
    set_points_y    = [375, 559]
    set_points_z1   = [ 54, 187]
    set_points_z2   = [ 54, 181]
    set_points_r    = [270, 245]
    set_points_t    = [  1,   1]


def Set_Point_Methane_Sources():
    # Methane Sources
    # 771 / 506 / 178 / 176 / 169
    global set_points_x, set_points_y, set_points_z1, set_points_z2, set_points_r, set_points_t

    set_points_x    = [796, 771]
    set_points_y    = [375, 541]
    set_points_z1   = [ 54, 192]
    set_points_z2   = [ 54, 185]
    set_points_r    = [270, 158]
    set_points_t    = [  1,   1]


def Set_Point_Black_Smoker():
    # Black Smoker
    # 918 / 32 / 68 / 62 / 136
    global set_points_x, set_points_y, set_points_z1, set_points_z2, set_points_r, set_points_t

    set_points_x    = [796, 918]
    set_points_y    = [375,  32]
    set_points_z1   = [ 54,  68]
    set_points_z2   = [ 54,  62]
    set_points_r    = [270, 136]
    set_points_t    = [  1,   1]


def Set_Point_Examine_Fireflies():
    # Examine Fireflies
    # 560 / 71 / 185 / 175 / 304
    global set_points_x, set_points_y, set_points_z1, set_points_z2, set_points_r, set_points_t

    set_points_x    = [796, 560, 560]
    set_points_y    = [375,  71,  71]
    set_points_z1   = [ 54, 130, 185]
    set_points_z2   = [ 54, 130, 175]
    set_points_r    = [270, 304, 304]
    set_points_t    = [  1,   1,   1]


class SetPoint:
    def __init__(self):
        self.pos_x = 0
        self.pos_y = 0
        self.pos_z1 = 0
        self.pos_z2 = 0
        self.pos_r = 0

    def reset(self):
        self.pos_x = 0
        self.pos_y = 0
        self.pos_z1 = 0
        self.pos_z2 = 0
        self.pos_r = 0
        return True

    def set(self, array):
        self.pos_x, self.pos_y, self.pos_z1, self.pos_z2, self.pos_r = array
        return True

    def printout(self):
        print("X: {0} , Y: {1} , Z1: {2} , Z2 {3} , R: {4}".format(self.pos_x, self.pos_y, self.pos_z1, self.pos_z2, self.pos_r))


class AutoSequence:
    def __init__(self):
        self.state = 0
        self.sequence_max = 0
        self.auto_mode = False
        self.auto_run = False
        self.auto_delay = False
        self.delay_time = 0
        self.end_seq = False
        self.end_seg_flag = False
        self.stop_flag = False

    def set_stop_flag(self):
        self.stop_flag = True

    def reset_stop_flag(self):
        self.stop_flag = False

    def get_stop_flag(self):
        return self.stop_flag

    def sequence_run(self):
        if self.state > 0:
            return True
        return False

    def set_sequence_max(self, value):
        self.sequence_max = value
        return True

    def get_sequence_max(self):
        return self.sequence_max

    def set_auto_mode(self):
        self.auto_mode = True
        return True

    def reset_auto_mode(self):
        self.auto_mode = False

    def get_auto_mode(self):
        return self.auto_mode

    def set_auto_delay(self):
        self.auto_delay = True

    def reset_auto_delay(self):
        self.auto_delay = False

    def get_auto_delay(self):
        return self.auto_delay

    def set_auto_run(self):
        self.auto_run = True

    def reset_auto_run(self):
        self.auto_run = False

    def get_auto_run(self):
        return self.auto_run

    def set_delay_time(self, value):
        self.delay_time = value

    def get_delay_time(self):
        return self.delay_time

    def set_state(self, value):
        self.state = value
        return True

    def get_state(self):
        return self.state

    def do_state_inc(self):
        if self.state < self.sequence_max:
            self.state += 1
            return True
        return False

    def is_last_state(self):
        if self.state >= self.sequence_max:
            return True
        return False

    def set_end_seq(self, value):
        self.end_seq = value

    def get_end_seq(self):
        return self.end_seq

    def is_end_seq_set(self):
        if self.end_seq and not self.end_seg_flag:
            self.end_seg_flag = True
            return True
        if not self.end_seq and self.end_seg_flag:
            self.end_seg_flag = False
        return False


def get_setpoint_array(num):
    value_array = set_points_x[num], set_points_y[num], set_points_z1[num], set_points_z1[num], set_points_r[num]
    return value_array


def main():
    global autosequence
    global setpoint, actpoint

    autosequence = AutoSequence()

    setpoint = SetPoint()
    actpoint = SetPoint()

    Set_Point_Mine_Crystals()

    autosequence.set_sequence_max(len(set_points_x))
    print(autosequence.get_sequence_max())
    print(autosequence.get_state())

    for x in range(0, 10):
        print("{0} , {1} ".format(x, autosequence.get_state()))
        if not autosequence.is_last_state():
            print("Inc")
            setpoint.set(get_setpoint_array(autosequence.get_state()))
            setpoint.printout()
        autosequence.do_state_inc()

    actpoint.printout()
    actpoint.set(get_setpoint_array(1))


if __name__ == "__main__":
    main()
