#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import sys
import pygame
import threading
import time

from serial_connection import *
from serial_commands import *
from serial_message import *
from uboot_functions import *
from auto_mode import *
from network_state import *

import socket
import random
import copy

from eurex_messages_short import states, Sample

# TCP_IP = '127.0.0.1'
TCP_IP = '192.168.178.201'
TCP_PORT = 5005
BUFFER_SIZE = 64  # Normally 1024, but we want fast response

restart_time = 0.1
auto_delay_time = 3

joystick_loop_mode = False
joystick_debug = False
key_debug = True
debug_printout = False

ref_pos_x = 51350
ref_pos_y = 35300
ref_pos_z = 2000
ref_pos_r = 0

task_network_break = 0

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

screen_w = 1024
screen_h = 768

uboot_offset_x = 0
uboot_offset_y = 0

sprite_angle_new = 0
sprite_angle_old = 0


def timer_call():
    global task_timer
    call_function()
    task_timer = threading.Timer(restart_time, timer_call)
    task_timer.start()


def call_function():
    global joystickinput
    # Start the function every restart_time
    # print("Test")
    if joystickinput.run_exit:
        # Nur hier auf die Serielle Schnittstelle schreiben
        update_position()


def wait_timer_start(delay_time=3):
    global wait_timer
    # print("Timer Start")
    wait_timer = threading.Timer(delay_time, wait_timer_call)
    wait_timer.start()


def wait_timer_call():
    global wait_timer
    global autosequence
    # print("Timer Call")
    autosequence.reset_auto_delay()


def task_network(task_network_state):
    global task_network_break
    print("Task Network start")
    # while True:
        # print("Task Network running")
        # if task_network_break == 1:
            # break
    network_server()
    print("Task Network end")
    return


def network_server():
    global n_state
    print("Start -> Network Server")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((TCP_IP, TCP_PORT))
    s.listen(1)

    while 1:
        conn, addr = s.accept()
        n_state.set_connect(True)
        print('Connection address: ', addr)
        sample = Sample()
        received_sample = Sample()

        while 1:
            data = conn.recv(BUFFER_SIZE)
            if not data:  # EOF
                break
            # print("received data: ", data)
            received_sample.deserialize(data)

            n_state.set_state(received_sample.flags1)
            # print("State changed from '{0} to '{1}'".format(sample.flags1, received_sample.flags1))

            sample = copy.copy(received_sample)
            del data

        n_state.set_connect(False)
        print("Connection was closed")
        conn.close()


class TextPrint:
    def __init__(self):
        self.reset()
        self.font = pygame.font.Font(None, 24)

    def plint(self, screen, textString):
        textBitmap = self.font.render(textString, True, WHITE)
        screen.blit(textBitmap, [self.x, self.y])
        self.y += self.line_height

    def reset(self):
        self.x = 10
        self.y = 10
        self.line_height = 20

    def indent(self):
        self.x += 10

    def unindent(self):
        self.x -= 10


def load_image(i):
    # load an image from the data directory with per pixel alpha transparency.
    return pygame.image.load(os.path.join("data", i)).convert_alpha()


def name_rotate_image(i):
    return "uboot-"+str(i)+".png"


def r_angle_clamp(a):
    return a % 360


def sprite_angle(a, step=15):
    y = step * (round((a) / step))
    if y > 359:
        y = 0
    return int(y)


# Wird alle restart_time aufgerufen
def update_position():
    global joystickinput
    global position_uboot
    global position_stepper
    global autosequence, setpoint, actpoint
    # global button_ext_start, button_ext_stop
    global ser
    global n_state

    if not joystick_loop_mode:
        # Position abfragen
        receive = serial_send_receive(command_pos())
        message.deserialize(receive)
        # message.printout()      # Debug
        position_stepper = message      # Positionswerte auf Objekt kopieren

        position_uboot.pos_x = x_skalieren(position_stepper.pos_x)
        position_uboot.pos_y = y_skalieren(position_stepper.pos_y)
        position_uboot.pos_z1 = z_skalieren(position_stepper.pos_z1)
        position_uboot.pos_z2 = z_skalieren(position_stepper.pos_z2)
        position_uboot.pos_r = r_skalieren(position_stepper.pos_r)

        # Positionswerte kopieren
        actpoint.pos_x = position_uboot.pos_x
        actpoint.pos_y = position_uboot.pos_y
        actpoint.pos_z1 = position_uboot.pos_z1
        actpoint.pos_z2 = position_uboot.pos_z2
        actpoint.pos_r = position_uboot.pos_r

        decode_joystick()

    else:
        joystick_loopback()

    # Hardwaretasten auswerten
    #decode_ext_button(position_stepper.status)
    decode_ext_button(joystickinput.debug)

    if n_state.has_change():
        # print("Netzwerkstatus geändert")
        network_decode()


def network_decode():
    global ser
    global n_state

    if n_state.get_state() == 0:
        print("VR-Reset")
        Set_Point_Start()
        receive = serial_send_receive(command_out_1_off())
        # receive = serial_send_receive(command_debug_off())
        # receive = serial_send_receive(command_out_2_on())

    if n_state.get_state() == 1:
        print("VR-Intro")
        Set_Point_Start()
        receive = serial_send_receive(command_out_1_off())
        # receive = serial_send_receive(command_debug_off())
        # receive = serial_send_receive(command_out_2_on())

    if n_state.get_state() == 2:
        print("VR-Win")
        Set_Point_Start()
        receive = serial_send_receive(command_out_1_off())
        # receive = serial_send_receive(command_debug_off())
        # receive = serial_send_receive(command_out_2_on())

    if n_state.get_state() == 3:
        print("VR-Loose")
        Set_Point_Start()
        receive = serial_send_receive(command_out_1_off())
        # receive = serial_send_receive(command_debug_off())
        # receive = serial_send_receive(command_out_2_on())

    if n_state.get_state() == 4:
        print("VR-Pause")
        # receive = serial_send_receive(command_out_1_on())
        # receive = serial_send_receive(command_debug_on())
        # receive = serial_send_receive(command_out_2_on())

    if n_state.get_state() == 5:
        print("VR-Task: Dispatch Cargo")
        Set_Point_Start()
        receive = serial_send_receive(command_out_1_on())
        # receive = serial_send_receive(command_debug_on())
        # receive = serial_send_receive(command_out_2_on())

    if n_state.get_state() == 6:
        print("VR-Task: Mine Crystals")
        Set_Point_Mine_Crystals()
        receive = serial_send_receive(command_out_1_on())
        # receive = serial_send_receive(command_debug_on())
        # receive = serial_send_receive(command_out_2_on())

    if n_state.get_state() == 7:
        print("VR-Task: Sample Methane Sources")
        Set_Point_Methane_Sources()
        receive = serial_send_receive(command_out_1_on())
        # receive = serial_send_receive(command_debug_on())
        # receive = serial_send_receive(command_out_2_on())

    if n_state.get_state() == 8:
        print("VR-Task: Measure Black Smoker")
        Set_Point_Black_Smoker()
        receive = serial_send_receive(command_out_1_on())
        # receive = serial_send_receive(command_debug_on())
        # receive = serial_send_receive(command_out_2_on())

    if n_state.get_state() == 9:
        print("VR-Task: Examine Fireflies")
        Set_Point_Examine_Fireflies()
        receive = serial_send_receive(command_out_1_on())
        # receive = serial_send_receive(command_debug_on())
        # receive = serial_send_receive(command_out_2_on())


def decode_ext_button(value):
    global button_ext_start, button_ext_stop

    button_ext_start.set_state(value & 0b01000000)
    button_ext_stop.set_state(value & 0b10000000)


def decode_joystick():
    global joystickinput
    global speed_uboot
    global button_ext_start, button_ext_stop
    global wait_timer
    global ser
    global auto_mode
    global autosequence, setpoint, actpoint

    if joystickinput.is_button_6_pressed():
        autosequence.auto_mode = False
        autosequence.reset_auto_run()
        autosequence.set_state(0)
        autosequence.set_end_seq(False)
        autosequence.reset_stop_flag()
        positionvalid.reset()

    if not autosequence.auto_mode:  # Auto-Sequence Mode Off
        if joystickinput.is_button_4_pressed():
            # print("Joystick-Taste 4 wurde gedrückt")
            # receive = serial_send_receive(command_ref_off())
            # print(receive)
            serial_send_receive(command_xpp(ref_pos_x))
            serial_send_receive(command_ypp(ref_pos_y))
            serial_send_receive(command_zpp(ref_pos_z))
            serial_send_receive(command_rpp(ref_pos_r))
            autosequence.set_state(0)
            autosequence.set_sequence_max(len(set_points_x))
            autosequence.auto_mode = True
            setpoint.set(get_setpoint_array(autosequence.get_state()))
            autosequence.set_delay_time(set_points_t[autosequence.get_state()])
            # setpoint.printout()

        if joystickinput.is_key_0_pressed():
            print("Keyboard-Taste 0 wurde gedrückt")
            serial_send_receive(command_xpn())
            serial_send_receive(command_ypn())
            serial_send_receive(command_zpn())
            serial_send_receive(command_rpn())

        # Y-Ache
        if joystickinput.is_left():
            if speed_uboot.y_speed_inc():
                # print("inc pos")
                # print(speed_uboot.get_y_speed_pwm())
                serial_send_receive(command_yfp(speed_uboot.get_y_speed_pwm()))     # Y-Achse positiv

        if joystickinput.is_right():
            if speed_uboot.y_speed_inc():
                # print("inc neg")
                # print(speed_uboot.get_y_speed_pwm())
                serial_send_receive(command_yfn(speed_uboot.get_y_speed_pwm()))     # Y-Achse negativ

        if joystickinput.is_x_mid():
            if speed_uboot.y_speed_dec():
                # print("dec")
                # print(speed_uboot.get_y_speed_pwm())
                serial_send_receive(command_yfs(speed_uboot.get_y_speed_pwm()))     # Y-Achse Frequenz
            else:
                if speed_uboot.y_speed_stop():
                    # print("Stop")
                    serial_send_receive(command_yst())      # Y-Achse STOP

        # X-Achse
        if joystickinput.is_up():
            if speed_uboot.x_speed_inc():
                # print("inc pos")
                # print(speed_uboot.get_x_speed_pwm())
                serial_send_receive(command_xfp(speed_uboot.get_x_speed_pwm()))     # X-Achse positiv

        if joystickinput.is_down():
            if speed_uboot.x_speed_inc():
                # print("inc neg")
                # print(speed_uboot.get_x_speed_pwm())
                serial_send_receive(command_xfn(speed_uboot.get_x_speed_pwm()))     # X-Achse negativ

        if joystickinput.is_y_mid():
            if speed_uboot.x_speed_dec():
                # print("dec")
                # print(speed_uboot.get_x_speed_pwm())
                serial_send_receive(command_xfs(speed_uboot.get_x_speed_pwm()))     # X-Achse Frequenz
            else:
                if speed_uboot.x_speed_stop():
                    # print("Stop")
                    serial_send_receive(command_xst())      # X-Achse STOP

        # Z1-Achse
        if joystickinput.get_button_0() and not joystickinput.get_button_2():
            if speed_uboot.z1_speed_inc():
                # print("inc pos")
                # print(speed_uboot.get_z1_speed_pwm())
                serial_send_receive(command_z1fn(speed_uboot.get_z1_speed_pwm()))  # Z1-Achse negativ

        if joystickinput.get_button_2() and not joystickinput.get_button_0():
            if speed_uboot.z1_speed_inc():
                # print("inc pos")
                # print(speed_uboot.get_z1_speed_pwm())
                serial_send_receive(command_z1fp(speed_uboot.get_z1_speed_pwm()))  # Z1-Achse positiv

        if not joystickinput.get_button_0() and not joystickinput.get_button_2():
            if speed_uboot.z1_speed_dec():
                # print("dec")
                # print(speed_uboot.get_z1_speed_pwm())
                serial_send_receive(command_z1fs(speed_uboot.get_z1_speed_pwm()))  # Z1-Achse Frequenz
            else:
                if speed_uboot.z1_speed_stop():
                    # print("Stop")
                    serial_send_receive(command_z1st())     # Z1-Achse STOP

        # Z2-Achse
        if joystickinput.get_button_1() and not joystickinput.get_button_3():
            if speed_uboot.z2_speed_inc():
                # print("inc pos")
                # print(speed_uboot.get_z2_speed_pwm())
                serial_send_receive(command_z2fn(speed_uboot.get_z2_speed_pwm()))  # Z2-Achse negativ

        if joystickinput.get_button_3() and not joystickinput.get_button_1():
            if speed_uboot.z2_speed_inc():
                # print("inc pos")
                # print(speed_uboot.get_z2_speed_pwm())
                serial_send_receive(command_z2fp(speed_uboot.get_z2_speed_pwm()))  # Z2-Achse positiv

        if not joystickinput.get_button_1() and not joystickinput.get_button_3():
            if speed_uboot.z2_speed_dec():
                # print("dec")
                # print(speed_uboot.get_z2_speed_pwm())
                serial_send_receive(command_z2fs(speed_uboot.get_z2_speed_pwm()))  # Z2-Achse Frequenz
            else:
                if speed_uboot.z2_speed_stop():
                    # print("Stop")
                    serial_send_receive(command_z2st())     # Z2-Achse STOP

        # R-Achse
        if joystickinput.get_button_5() and not joystickinput.get_button_7():
            if speed_uboot.r_speed_inc():
                # print("inc pos")
                # print(speed_uboot.get_r_speed_pwm())
                serial_send_receive(command_rfp(speed_uboot.get_r_speed_pwm()))  # R-Achse positiv

        if joystickinput.get_button_7() and not joystickinput.get_button_5():
            if speed_uboot.r_speed_inc():
                # print("inc pos")
                # print(speed_uboot.get_r_speed_pwm())
                serial_send_receive(command_rfn(speed_uboot.get_r_speed_pwm()))  # R-Achse positiv

        if not joystickinput.get_button_5() and not joystickinput.get_button_7():
            if speed_uboot.r_speed_dec():
                # print("dec")
                # print(speed_uboot.get_r_speed_pwm())
                serial_send_receive(command_rfs(speed_uboot.get_r_speed_pwm()))  # Z2-Achse STOP
            else:
                if speed_uboot.r_speed_stop():
                    # print("Stop")
                    serial_send_receive(command_rst())

    else:                           # Auto-Sequence Mode On

        # if joystickinput.is_key_1_pressed() and not autosequence.auto_run:
        if button_ext_start.is_pressed() or joystickinput.is_key_1_pressed():
            if not autosequence.auto_run and not autosequence.sequence_run():
                print("Start-Taste wurde gedrückt")
                # Start Autosequence -----------------------------------------------------------------------------------
                # hier muss noch was Code hin
                autosequence.set_state(0)
                setpoint.set(get_setpoint_array(autosequence.get_state()))
                # setpoint.printout()
                autosequence.set_end_seq(False)
                positionvalid.reset()
                autosequence.set_auto_run()
            else:
                if autosequence.get_stop_flag():
                    print("Restart")
                    autosequence.reset_stop_flag()
                    autosequence.set_auto_run()

        if button_ext_stop.is_pressed() or joystickinput.is_key_2_pressed():
            if autosequence.sequence_run():
                print("Stop-Taste wurde gedrückt")
                autosequence.set_stop_flag()
                autosequence.reset_auto_run()
                serial_send_receive(command_xst())
                serial_send_receive(command_yst())
                serial_send_receive(command_z1st())
                serial_send_receive(command_z2st())
                serial_send_receive(command_rst())
                positionvalid.reset()
                speed_uboot.reset_value()


        # Sollposition erreicht
        if positionvalid.is_pos_okay():
            # print("Sende STOP an alle Achsen")
            serial_send_receive(command_xst())
            serial_send_receive(command_yst())
            serial_send_receive(command_z1st())
            serial_send_receive(command_z2st())
            serial_send_receive(command_rst())
            positionvalid.reset()
            autosequence.set_delay_time(set_points_t[autosequence.get_state()])
            autosequence.do_state_inc()
            if not autosequence.is_last_state():
                # print("Sequence run")
                # print(autosequence.state)
                # print(autosequence.sequence_max)
                setpoint.set(get_setpoint_array(autosequence.get_state()))
                # setpoint.printout()
                autosequence.set_auto_delay()
                wait_timer_start(autosequence.get_delay_time())  # Sequence Delay Timer starten -> gibt autosequence.reset_auto_delay() zurück
                # autosequence.reset_auto_delay()

            else:
                autosequence.reset_auto_run()
                autosequence.set_end_seq(True)
                autosequence.set_state(0)
                # print("End Sequence")


        if autosequence.auto_run and not autosequence.auto_delay:
            # Fahrt bei Differenz
            get_pos_diff(actpoint, setpoint)

        if autosequence.is_end_seq_set():
                # print("Sende STOP an alle Achsen")
                serial_send_receive(command_xst())
                serial_send_receive(command_yst())
                serial_send_receive(command_z1st())
                serial_send_receive(command_z2st())
                serial_send_receive(command_rst())


def get_pos_diff(act_p, set_p):
    global ser
    global speed_uboot
    global positionvalid
    global autosequence

    # print("X: {0} , Y: {1} , Z1: {2} , Z2 {3} , R: {4}".format(act_p.pos_x, act_p.pos_y, act_p.pos_z1, act_p.pos_z2, act_p.pos_r))
    # print("X: {0} , Y: {1} , Z1: {2} , Z2 {3} , R: {4}".format(set_p.pos_x, set_p.pos_y, set_p.pos_z1, set_p.pos_z2, set_p.pos_r))

    # X-Achse
    if True:
        if act_p.pos_x + pos_diff_x < set_p.pos_x:
            # print("X-Achse fahre pos")
            if speed_uboot.x_speed_inc():
                serial_send_receive(command_xfp(speed_uboot.get_x_speed_pwm()))  # X-Achse positiv
        else:
            if act_p.pos_x - pos_diff_x > set_p.pos_x:
                # print("X-Achse fahre neg")
                if speed_uboot.x_speed_inc():
                    serial_send_receive(command_xfn(speed_uboot.get_x_speed_pwm()))  # X-Achse positiv
            else:
                # print("X-Achse STOP")
                # positionvalid.set_valid_x(True)
                if speed_uboot.x_speed_dec():
                    serial_send_receive(command_xfs(speed_uboot.get_x_speed_pwm()))  # X-Achse STOP
                else:
                    positionvalid.set_valid_x(True)
                    if speed_uboot.x_speed_stop():
                        serial_send_receive(command_xst())
                        # print("X-Achse STOP")

    # Y-Achse
    if True:
        if act_p.pos_y + pos_diff_y < set_p.pos_y:
            # print("Y-Achse fahre pos")
            if speed_uboot.y_speed_inc():
                serial_send_receive(command_yfp(speed_uboot.get_y_speed_pwm()))  # Y-Achse positiv
        else:
            if act_p.pos_y - pos_diff_y > set_p.pos_y:
                # print("Y-Achse fahre neg")
                if speed_uboot.y_speed_inc():
                    serial_send_receive(command_yfn(speed_uboot.get_y_speed_pwm()))  # Y-Achse positiv
            else:
                # print("Y-Achse STOP")
                # positionvalid.set_valid_y(True)
                if speed_uboot.y_speed_dec():
                    serial_send_receive(command_yfs(speed_uboot.get_y_speed_pwm()))  # Y-Achse STOP
                else:
                    positionvalid.set_valid_y(True)
                    if speed_uboot.y_speed_stop():
                        serial_send_receive(command_yst())
                        # print("Y-Achse STOP")

    # Z1-Achse
    if True:
        if act_p.pos_z1 + pos_diff_z < set_p.pos_z1:
            # print("Z1-Achse fahre pos")
            if speed_uboot.z1_speed_inc():
                serial_send_receive(command_z1fp(speed_uboot.get_z1_speed_pwm()))  # Z1-Achse positiv
        else:
            if act_p.pos_z1 - pos_diff_z > set_p.pos_z1:
                # print("Z1-Achse fahre neg")
                if speed_uboot.z1_speed_inc():
                    serial_send_receive(command_z1fn(speed_uboot.get_z1_speed_pwm()))  # Z1-Achse positiv
            else:
                # print("Z1-Achse STOP")
                # positionvalid.set_valid_z1(True)
                if speed_uboot.z1_speed_dec():
                    serial_send_receive(command_z1fs(speed_uboot.get_z1_speed_pwm()))  # Z1-Achse STOP
                else:
                    positionvalid.set_valid_z1(True)
                    if speed_uboot.z1_speed_stop():
                        serial_send_receive(command_z1st())
                        # print("Z1-Achse STOP")

    # Z2-Achse
    if True:
        if act_p.pos_z2 + pos_diff_z < set_p.pos_z2:
            # print("Z2-Achse fahre pos")
            if speed_uboot.z2_speed_inc():
                serial_send_receive(command_z2fp(speed_uboot.get_z2_speed_pwm()))  # Z2-Achse positiv
        else:
            if act_p.pos_z2 - pos_diff_z > set_p.pos_z2:
                # print("Z2-Achse fahre neg")
                if speed_uboot.z2_speed_inc():
                    serial_send_receive(command_z2fn(speed_uboot.get_z2_speed_pwm()))  # Z2-Achse positiv
            else:
                # print("Z2-Achse STOP")
                # positionvalid.set_valid_z2(True)
                if speed_uboot.z2_speed_dec():
                    serial_send_receive(command_z2fs(speed_uboot.get_z2_speed_pwm()))  # Z2-Achse STOP
                else:
                    positionvalid.set_valid_z2(True)
                    if speed_uboot.z2_speed_stop():
                        serial_send_receive(command_z2st())
                        # print("Z2-Achse STOP")

    # R-Achse
    if True:

        delta_r = get_r_delta(act_p.pos_r, set_p.pos_r)

        if delta_r + pos_diff_r < 0:
            # print("R-Achse fahre pos")
            if speed_uboot.r_speed_inc():
                serial_send_receive(command_rfp(speed_uboot.get_r_speed_pwm()))  # R-Achse positiv
        else:
            if delta_r - pos_diff_r > 0:
                # print("R-Achse fahre neg")
                if speed_uboot.r_speed_inc():
                    serial_send_receive(command_rfn(speed_uboot.get_r_speed_pwm()))  # R-Achse positiv
            else:
                # print("R-Achse STOP")
                # positionvalid.set_valid_r(True)
                if speed_uboot.r_speed_dec():
                    serial_send_receive(command_rfs(speed_uboot.get_r_speed_pwm()))  # R-Achse STOP
                else:
                    positionvalid.set_valid_r(True)
                    if speed_uboot.r_speed_stop():
                        serial_send_receive(command_rst())
                        # print("R-Achse STOP")


def get_r_delta(ist, soll):
    if ist - soll > 180:
        return -(360 + soll - ist)
    else:
        if soll - ist > 180:
            return -(360 + ist - soll)
        return ist - soll

# ----------------------------------------------------------------------------------------------------------------------
# --- PyGame loop                                                                                                    ---
# ----------------------------------------------------------------------------------------------------------------------


def play_game():
    global joystickinput, position_stepper, position_uboot, speed_uboot, autosequence, positionvalid
    global button_input, switch_start, switch_start_flag, switch_stop, switch_stop_flag, state_mem, auto_mode
    global pos_stepper, pos_uboot, speed_uboot
    global state_byte_1, state_byte_2, status_flags
    global sprite_angle_new, sprite_angle_old
    global freq_value
    global set_x_max, set_y_max, set_z_max, ref_value
    global n_state

    pygame.init()

    pygame.display.init()
    pygame.font.init()

    # Set the width and height of the screen [width,height]
    size = [screen_w, screen_h]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("UBoot-Simulation")
    # Set Keyboard Repeat Rate
    pygame.key.set_repeat(500, 2)

    # Loop until the user clicks the close button.
    done = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    screen.fill(BLACK)
    pygame.display.flip()

    terrain1 = load_image("terrain-01.png")
    uboot = load_image(name_rotate_image(0))

    # create a mask for each of them.
    terrain1_mask = pygame.mask.from_surface(terrain1, 50)
    uboot_mask = pygame.mask.from_surface(uboot, 50)

    # this is where the uboot, and terrain are.
    terrain1_rect = terrain1.get_rect()
    uboot_rect = uboot.get_rect()

    # a message for if the uboot hits the terrain.
    afont = pygame.font.Font(None, 24)
    hitsurf = afont.render("Kontakt", 1, (255, 255, 255))

    last_bx, last_by = 0, 0

    uboot_rect.x = uboot_offset_x
    uboot_rect.y = uboot_offset_y

    # Get ready to print
    textPrint = TextPrint()

    # Initialize the joysticks
    pygame.joystick.init()

    # Get count of joysticks
    joystick_count = pygame.joystick.get_count()

    # For each joystick:
    for i in range(joystick_count):
        joystick = pygame.joystick.Joystick(i)
        joystick.init()

    joystickinput.run_exit = True

    # -------- Main Program Loop -----------
    while done == False:
        # EVENT PROCESSING STEP
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                done = True  # Flag that we are done so we exit this loop
                joystickinput.run_exit = False

            # Possible joystick actions: JOYAXISMOTION JOYBALLMOTION JOYBUTTONDOWN JOYBUTTONUP JOYHATMOTION
            # Joystick X/Y abfragen
            if event.type == pygame.JOYAXISMOTION:
                #print("Joystick X/Y Axis")
                axis_0 = round(joystick.get_axis(0))
                axis_1 = round(joystick.get_axis(1))
                if axis_0 == -1:
                    joystickinput.left = 1
                if axis_0 == 0:
                    joystickinput.left = 0
                    joystickinput.right = 0
                if axis_0 == +1:
                    joystickinput.right = 1
                if axis_1 == -1:
                    joystickinput.up = 1
                if axis_1 == 0:
                    joystickinput.up = 0
                    joystickinput.down = 0
                if axis_1 == +1:
                    joystickinput.down = 1
            # Tasten abfragen
            if event.type == pygame.JOYBUTTONDOWN:
                if joystick.get_button(0) == 1:
                    joystickinput.button_0 = 1
                if joystick.get_button(1) == 1:
                    joystickinput.button_1 = 1
                if joystick.get_button(2) == 1:
                    joystickinput.button_2 = 1
                if joystick.get_button(3) == 1:
                    joystickinput.button_3 = 1
                if joystick.get_button(4) == 1:
                    joystickinput.button_4 = 1
                if joystick.get_button(5) == 1:
                    joystickinput.button_5 = 1
                if joystick.get_button(6) == 1:
                    joystickinput.button_6 = 1
                if joystick.get_button(7) == 1:
                    joystickinput.button_7 = 1
            if event.type == pygame.JOYBUTTONUP:
                if joystick.get_button(0) == 0:
                    joystickinput.button_0 = 0
                if joystick.get_button(1) == 0:
                    joystickinput.button_1 = 0
                if joystick.get_button(2) == 0:
                    joystickinput.button_2 = 0
                if joystick.get_button(3) == 0:
                    joystickinput.button_3 = 0
                if joystick.get_button(4) == 0:
                    joystickinput.button_4 = 0
                if joystick.get_button(5) == 0:
                    joystickinput.button_5 = 0
                if joystick.get_button(6) == 0:
                    joystickinput.button_6 = 0
                if joystick.get_button(7) == 0:
                    joystickinput.button_7 = 0
            # Tastatur abfrgen
            # Key down
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_0:
                    joystickinput.key_0 = 1
                if event.key == pygame.K_1:
                    joystickinput.key_1 = 1
                if event.key == pygame.K_2:
                    joystickinput.key_2 = 1
                if key_debug:
                    if event.key == pygame.K_F1:
                        joystickinput.debug = 128
                    if event.key == pygame.K_F2:
                        joystickinput.debug = 64
            # Key up
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_0:
                    joystickinput.key_0 = 0
                if event.key == pygame.K_1:
                    joystickinput.key_1 = 0
                if event.key == pygame.K_2:
                    joystickinput.key_2 = 0
                if key_debug:
                    if event.key == pygame.K_F1:
                        joystickinput.debug = 192
                    if event.key == pygame.K_F2:
                        joystickinput.debug = 192

        if joystick_debug:
            # Debug -> Ausgabe der Joystick Werte
            print(joystickinput.printout())


        # see how far the uboot rect is offset from the terrain rect.
        bx, by = (uboot_rect[0], uboot_rect[1])
        offset_x = bx - terrain1_rect[0]
        offset_y = by - terrain1_rect[1]

        # print bx, by
        overlap = terrain1_mask.overlap(uboot_mask, (offset_x, offset_y))

        uboot_rect.x = uboot_offset_x + (screen_w * position_uboot.pos_x / 1168)
        uboot_rect.y = uboot_offset_y + (screen_h * position_uboot.pos_y / 900)
        #
        last_bx, last_by = bx, by

        # draw the background color, and the terrain.
        screen.fill((0, 0, 100))
        screen.blit(terrain1, (0, 0))

        # draw the uboot.
        screen.blit(uboot, (uboot_rect[0], uboot_rect[1]))

        # draw the uboot rect, so you can see where the bounding rect would be.
        # pygame.draw.rect(screen, (0, 0, 255), uboot_rect, 1)


        textPrint.reset()
        #textPrint.plint(screen, "Number of joysticks: {}".format(joystick_count))
        #textPrint.indent()
        textPrint.plint(screen, "X-: S: {0:5d} ; U: {1:5d} ; X-Speed {2:5d}".format(position_stepper.pos_x, position_uboot.pos_x, speed_uboot.get_x_speed_act()))
        textPrint.plint(screen, "Y-: S: {0:5d} ; U: {1:5d} ; Y-Speed {2:5d}".format(position_stepper.pos_y, position_uboot.pos_y, speed_uboot.get_y_speed_act()))
        textPrint.plint(screen, "Z1-: S: {0:5d} ; U: {1:5d} ; Z1-Speed {2:5d}".format(position_stepper.pos_z1, position_uboot.pos_z1, speed_uboot.get_z1_speed_act()))
        textPrint.plint(screen, "Z2-: S: {0:5d} ; U: {1:5d} ; Z2-Speed {2:5d}".format(position_stepper.pos_z2, position_uboot.pos_z2, speed_uboot.get_z2_speed_act()))
        textPrint.plint(screen, "R-: S: {0:5d} ; U: {1:5d} ; R-Speed {2:5d}".format(position_stepper.pos_r, r_angle_clamp(position_uboot.pos_r), speed_uboot.get_r_speed_act()))
        textPrint.plint(screen, "Status: {0:3d} ".format(position_stepper.status))
        textPrint.plint(screen, "Auto-Mode: {0:2d} ; -Run: {1:2d} ; -Seq: {2:2d} ; -Delay: {3:2d} ; -Time: {4:2d}".format(autosequence.get_auto_mode(), autosequence.get_auto_run(), autosequence.get_state(), autosequence.get_auto_delay(), autosequence.get_delay_time()))
        if key_debug:
            textPrint.plint(screen, "Debug: {0:3d} ".format(joystickinput.debug))
        if debug_printout:
            textPrint.plint(screen, "Sequence_Max: {0}".format(autosequence.get_sequence_max()))
        textPrint.plint(screen, "X: {0} ; Y: {1} ; Z1: {2} ; Z2: {3} ; R: {4}".format(int(positionvalid.get_valid_x()),
                                                                                      int(positionvalid.get_valid_y()),
                                                                                      int(positionvalid.get_valid_z1()),
                                                                                      int(positionvalid.get_valid_z2()),
                                                                                      int(positionvalid.get_valid_r())))
        # textPrint.plint(screen, "Start-Knopf: {0:2d} ; Stop-Knopf: {1:2d} ; State-Mem: {2:2d} ; Auto-Mode: {3:2d}".format(switch_start, switch_stop, state_mem, auto_mode))
        textPrint.plint(screen, "Network-State: {0}".format(int(n_state.get_state())))

        sprite_angle_new = sprite_angle(r_angle_clamp(position_uboot.pos_r))
        if not sprite_angle_new == sprite_angle_old:
            sprite_angle_old = sprite_angle_new
            uboot = load_image(name_rotate_image(sprite_angle_new))


        # see if there was an overlap of pixels between the uboot
        #   and the terrain.
        #if overlap:
            # we have hit the wall!!!  oh noes!
            #screen.blit(hitsurf, (0, 0))
            #uboot = load_image("uboot-15.png")
            #uboot_mask = pygame.mask.from_surface(uboot, 50)
            #print("Kontakt")

        # flip the display.
        pygame.display.flip()

        # Limit to 20 frames per second
        clock.tick(20)


        # --------------------------------------------------------------------------------------------------------------

    # PyGame quit
    pygame.quit()

    # ------------------------------------------------------------------------------------------------------------------

# ======================================================================================================================
# ======================================================================================================================
# === Main
# ======================================================================================================================
# ======================================================================================================================
def main():
    global joystickinput
    global position_stepper
    global position_uboot
    global speed_uboot
    global task_timer
    global task_network_break
    # global wait_timer
    global message
    global autosequence, setpoint, actpoint, positionvalid
    global button_ext_start, button_ext_stop
    global n_state
    global ser

    message = Message()

    serial_init()

    joystickinput = JoyStickInput()

    n_state = NetWorkState()

    n_state.reset_state()

    position_stepper = PositionObj()
    position_uboot = PositionObj()

    speed_uboot = UBootObj()

    autosequence = AutoSequence()

    setpoint = SetPoint()
    actpoint = SetPoint()

    positionvalid = PositionValid()

    positionvalid.reset()

    button_ext_start = ExtButton()
    button_ext_stop = ExtButton()

    button_ext_start.set_state(0)
    button_ext_stop.set_state(0)

    print("Start")
    time.sleep(2)
    print("Sende Reset")

    time.sleep(0.1)

    print("Sende Enable")
    receive = serial_send_receive(command_xen_on())
    # print(receive.rstrip("\r\n"))
    receive = serial_send_receive(command_yen_on())
    # print(receive.rstrip("\r\n"))
    receive = serial_send_receive(command_zen_on())
    # print(receive.rstrip("\r\n"))
    receive = serial_send_receive(command_ren_on())
    # print(receive.rstrip("\r\n"))

    print("Sende Relais aus -> Zustand eingeschaltet")
    receive = serial_send_receive(command_out_1_off())
    receive = serial_send_receive(command_out_2_off())

    print("Timer_Call -> Start")
    timer_call()

    threads = []
    t = threading.Thread(target=task_network, args=("Task-1",))
    threads.append(t)
    t.start()
    print("Start Network Task")

    print("Main Wait 1 sec.")
    time.sleep(1)

    print("Start PyGame")
    play_game()
    print("Exit PyGame")

    time.sleep(1)
    print("Cancel Timer-Task")
    task_timer.cancel()

    time.sleep(1)
    print("Cancel Network Task")
    task_network_break = 1

    time.sleep(1)
    print("Sende Disable")
    receive = serial_send_receive(command_xen_off())
    # print(receive.rstrip("\r\n"))
    receive = serial_send_receive(command_yen_off())
    # print(receive.rstrip("\r\n"))
    receive = serial_send_receive(command_zen_off())
    # print(receive.rstrip("\r\n"))
    receive = serial_send_receive(command_ren_off())
    # print(receive.rstrip("\r\n"))
    print("Sende Relais aus")
    receive = serial_send_receive(command_out_1_off())
    receive = serial_send_receive(command_out_2_off())

    time.sleep(1)
    print("Serial Close")
    serial_close()


    print("Programm-Ende")


if __name__ == "__main__":
    main()
