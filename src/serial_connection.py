#!/usr/bin/python3
# -*- coding: utf-8 -*-

# import os
# import sys
import serial
import serial.tools.list_ports


class SerialCon:
    def __init__(self):
        self.connect = False
        self.com_port = 0
        self.state = 0
        self.last_state = 0

    def setstate(self, state):
        self.state = state

    def getstate(self):
        return self.state

    def get_usb_port(self):

        # serial_timeout = 1

        ports = list(serial.tools.list_ports.grep('USB'))

        if ports:
            return ports[0]
        else:
            return False


def unknown_func():

    if ports:
        try:
            serial_port = serial.Serial(        # open serial port
                port=com_port,
                baudrate=115200,
                parity=serial.PARITY_NONE,
                stopbits=serial.STOPBITS_ONE,
                bytesize=serial.EIGHTBITS,
                timeout=serial_timeout)

            print("Serial-Port: {0}".format(serial_port))
            SerialPort.com_port = serial_port
            return serial_port
        except:
            print("Could not open Port: {0}".format(com_port))

    else:
        return False


def serial_is_open():
    global serial_port
    try:
        if serial_port.isOpen():
            print("Serielle Verbindung: " + ser.portstr)
            return True
    except:
        print("Keine Serielle Verbindung")
        return False


def serial_input():
    global ser
    while True:
        reading = ser.readline().decode('utf-8')
        if len(reading) > 0:
            break

        reading = "Timeout"

    return reading


def serial_output(send):
    ser.write(send.encode())


def serial_send_receive(send):
    serial_output(send)
    return serial_input()


def serial_close():
    if serial_is_open():
        ser.close()


########################################################################################################################
# Main                                                                                                                 #
########################################################################################################################

def main():

    import time

    loop_forever = 1
    i = 0
    cmd_reset = "res\n"
    cmd_pos = "pos\n"

    if 0:
        if serial_init():

            print("Sende Reset Kommando")
            receive = serial_send_receive(cmd_reset)
            # print(receive.rstrip("\r\n"))
            if receive.rstrip("\r\n") == "6":
                print("Reset Kommando erfolgt")
            else:
                print("Keine Antwort")

            time.sleep(0.1)

            if loop_forever:
                print("Schleifentest")
                while i < 100:
                    i += 1
                    try:
                        receive = serial_send_receive(cmd_pos)
                    except:
                        serial_close()
                        # Kommunikation Senden Empfangen schlägt fehl
                        break
                    # print(receive.rstrip("\r\n"))
                    if receive.rstrip("\r\n"):
                        print("Position -> {0}".format(receive))
                    else:
                        print("Keine Antwort")
                        break

                    time.sleep(0.05)

            serial_close()

    if 1:
        ser_conn = SerialCon()
        print("Test")

        ser_conn.setstate(2)
        print(ser_conn.getstate())

        print(ser_conn.get_usb_port())

    print("Programm-Ende")


if __name__ == "__main__":
    main()
