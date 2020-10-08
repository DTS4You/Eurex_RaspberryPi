import serial

ser = serial.Serial()
ser.baudrate = 115200
ser.port = 'COM1'
# print(ser)
try:
    ser.open()
except serial.SerialException:
    print("Kann Com-Port nicht öffnen")
print(ser.is_open)
try:
    ser.close()
except serial.SerialException:
    print("Kann Com-Port nicht schliessen")
