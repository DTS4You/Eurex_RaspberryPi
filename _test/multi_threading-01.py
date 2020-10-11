import time
from threading import Thread


def sleeper(i):
    print("thread {} sleeps for {} seconds".format(i,i))
    time.sleep(i)
    print("thread %d woke up" % i)


def main():

    for i in range(10):
        t = Thread(target=sleeper, args=(i,))
        t.start()


###############################################################################
# Main
###############################################################################

if __name__ == '__main__':
    main()
