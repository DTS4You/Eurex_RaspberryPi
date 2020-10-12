import time
from threading import Thread


def sleeper(i):
    print("thread {} sleeps for {} seconds".format(i, i))
    time.sleep(i)
    print("thread %d woke up" % i)


def main():
    global t1, t2
    t1 = Thread(target=sleeper, args=(1, ))
    t1.start()
    t2 = Thread(target=sleeper, args=(2, ))
    t2.start()


###############################################################################
# Main
###############################################################################


if __name__ == '__main__':
    global t1, t2
    main()
    print("")
    print("Ende Main")

    t1.join()
    t2.join()

    print("Programm-Ende")

###############################################################################
