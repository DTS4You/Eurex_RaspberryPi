#!/usr/bin/python3
# -*- coding: utf-8 -*-

# from scale_functions import *
from uboot_functions import *

def x_skalieren(inkremente):
    return int(round((1024 / 49246) * inkremente))


def y_skalieren(inkremente):
    return int(round((768 / 34667) * inkremente))


def z_skalieren(inkremente):
    return int(round((1000 / 1957) * inkremente))


def r_skalieren(inkremente):
    return int(round((360 / 12800) * inkremente))


def update_position():
    global position_uboot
    global position_stepper
    # Wird alle restart_time aufgerufen

    position_uboot.pos_x = x_skalieren(position_stepper.pos_x)
    position_uboot.pos_y = y_skalieren(position_stepper.pos_y)
    position_uboot.pos_z1 = z_skalieren(position_stepper.pos_z1)
    position_uboot.pos_z2 = z_skalieren(position_stepper.pos_z2)
    position_uboot.pos_r = r_skalieren(position_stepper.pos_r)


def input_to_loop():
    pass


def clamp(x, minimum, maximum):
    return max(minimum, min(x, maximum))

# ----------------------------------------------------------------------------------------------------------------------

def main():
    pass


if __name__ == "__main__":
    main()

