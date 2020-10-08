#!/usr/bin/python3
# -*- coding: utf-8 -*-

# import os
# import sys
# import serial


# Reset Command
def command_res():
    cmd_string = "res\n"
    return cmd_string


def command_out_1_on():
    cmd_string = "out1,1\n"
    return cmd_string


def command_out_1_off():
    cmd_string = "out1,0\n"
    return cmd_string


def command_out_2_on():
    cmd_string = "out2,1\n"
    return cmd_string


def command_out_2_off():
    cmd_string = "out2,0\n"
    return cmd_string


def command_debug_on():
    cmd_string = "debug,1\n"
    return cmd_string


def command_debug_off():
    cmd_string = "debug,0\n"
    return cmd_string


# Positions Command
def command_pos():
    cmd_string = "pos\n"
    return cmd_string


# Enable Commands
def command_xen_on():
    cmd_string = "xen,1\n"
    return cmd_string


def command_xen_off():
    cmd_string = "xen,0\n"
    return cmd_string


def command_yen_on():
    cmd_string = "yen,1\n"
    return cmd_string


def command_yen_off():
    cmd_string = "yen,0\n"
    return cmd_string


def command_zen_on():
    cmd_string = "zen,1\n"
    return cmd_string


def command_zen_off():
    cmd_string = "zen,0\n"
    return cmd_string


def command_ren_on():
    cmd_string = "ren,1\n"
    return cmd_string


def command_ren_off():
    cmd_string = "ren,0\n"
    return cmd_string


# Refernz Command
def command_ref_on():
    cmd_string = "ref,1\n"
    return cmd_string


def command_ref_off():
    cmd_string = "ref,0\n"
    return cmd_string


# X-Axis Commands
def command_xfp(value):
    cmd_string = "xfp," + str(value) + "\n"
    return cmd_string


def command_xfn(value):
    cmd_string = "xfn," + str(value) + "\n"
    return cmd_string


def command_xdp():
    cmd_string = "xdp\n"
    return cmd_string


def command_xdn():
    cmd_string = "xdn\n"
    return cmd_string


def command_xfs(value):
    cmd_string = "xfs," + str(value) + "\n"
    return cmd_string


def command_xst():
    cmd_string = "xst\n"
    return cmd_string


# Y-Axis Commands
def command_yfp(value):
    cmd_string = "yfp," + str(value) + "\n"
    return cmd_string


def command_yfn(value):
    cmd_string = "yfn," + str(value) + "\n"
    return cmd_string


def command_yfs(value):
    cmd_string = "yfs," + str(value) + "\n"
    return cmd_string


def command_ydp():
    cmd_string = "ydp\n"
    return cmd_string


def command_ydn():
    cmd_string = "ydn\n"
    return cmd_string


def command_yst():
    cmd_string = "yst\n"
    return cmd_string


# Z-Axis Commands
def command_zfp(value):
    cmd_string = "zfp," + str(value) + "\n"
    return cmd_string


def command_zfn(value):
    cmd_string = "zfn," + str(value) + "\n"
    return cmd_string


def command_zfs(value):
    cmd_string = "zfs," + str(value) + "\n"
    return cmd_string


def command_zdp():
    cmd_string = "zdp\n"
    return cmd_string


def command_zdn():
    cmd_string = "zdn\n"
    return cmd_string


def command_zst():
    cmd_string = "zst\n"
    return cmd_string


# Z1 Axis Commands
def command_z1fp(value):
    cmd_string = "z1fp," + str(value) + "\n"
    return cmd_string


def command_z1fn(value):
    cmd_string = "z1fn," + str(value) + "\n"
    return cmd_string


def command_z2fp(value):
    cmd_string = "z2fp," + str(value) + "\n"
    return cmd_string


def command_z1dp():
    cmd_string = "z1dp\n"
    return cmd_string


def command_z1dn():
    cmd_string = "z1dn\n"
    return cmd_string


def command_z1st():
    cmd_string = "z1st\n"
    return cmd_string


# Z2 Axis Commands
def command_z2fn(value):
    cmd_string = "z2fn," + str(value) + "\n"
    return cmd_string


def command_z1fs(value):
    cmd_string = "z1fs," + str(value) + "\n"
    return cmd_string


def command_z2fs(value):
    cmd_string = "z2fs," + str(value) + "\n"
    return cmd_string


def command_z2dp():
    cmd_string = "z2dp\n"
    return cmd_string


def command_z2dn():
    cmd_string = "z2dn\n"
    return cmd_string


def command_z2st():
    cmd_string = "z2st\n"
    return cmd_string


# R-Axis Commands
def command_rfp(value):
    cmd_string = "rfp," + str(value) + "\n"
    return cmd_string


def command_rfn(value):
    cmd_string = "rfn," + str(value) + "\n"
    return cmd_string


def command_rfs(value):
    cmd_string = "rfs," + str(value) + "\n"
    return cmd_string


def command_rdp():
    cmd_string = "rdp\n"
    return cmd_string


def command_rdn():
    cmd_string = "rdn\n"
    return cmd_string


def command_rst():
    cmd_string = "rst\n"
    return cmd_string


# Positions Commands
def command_xpn():
    cmd_string = "xpn\n"
    return cmd_string


def command_ypn():
    cmd_string = "ypn\n"
    return cmd_string


def command_zpn():
    cmd_string = "zpn\n"
    return cmd_string


def command_rpn():
    cmd_string = "rpn\n"
    return cmd_string


def command_xpp(value):
    cmd_string = "xpp," + str(value) + "\n"
    return cmd_string


def command_ypp(value):
    cmd_string = "ypp," + str(value) + "\n"
    return cmd_string


def command_zpp(value):
    cmd_string = "zpp," + str(value) + "\n"
    return cmd_string


def command_rpp(value):
    cmd_string = "rpp," + str(value) + "\n"
    return cmd_string


def command_xpm(value):
    cmd_string = "xpm," + str(value) + "\n"
    return cmd_string


def command_ypm(value):
    cmd_string = "ypm," + str(value) + "\n"
    return cmd_string


def command_zpm(value):
    cmd_string = "zpm," + str(value) + "\n"
    return cmd_string




def main():

    # print(command_ypm(100))
    # print(command_zpm(100))

    return True


if __name__ == "__main__":
    main()
