import serial.tools.list_ports


def list_comports(search_port):
    ports = serial.tools.list_ports.comports()

    if ports:
        for p in ports:
            if search_port in p.description:
                # print(p.device)
                return p.device
        # print(len(ports), 'ports found')


def main():

    search_pattern = "CH340"

    result = list_comports(search_pattern)

    if result:
        print(result)
    else:
        print("No Com-Port found")


if __name__ == '__main__':
    main()
