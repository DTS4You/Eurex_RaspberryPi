import serial.tools.list_ports

ports = serial.tools.list_ports.comports()

if ports:
    for p in ports:
        com_port = p.device
        com_desc = p.description
        print(p.device, p.description)
    print(len(ports), 'ports found')

