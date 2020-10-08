
class NetWorkState:
    def __init__(self):
        self.connect = False
        self.state = 0
        self.last_state = 0

    def reset_state(self):
        self.state = 0
        self.last_state = 0

    def set_connect(self, value):
        self.connect = value
        return self.connect

    def get_connect(self):
        return self.connect

    def set_state(self, value):
        self.state = value
        return self.state

    def get_state(self):
        return self.state

    def has_change(self):
        if self.state == self.last_state:
            return False
        else:
            self.last_state = self.state
            return True


# ======================================================================================================================
# === Main
#=======================================================================================================================
def main():

    n_state = NetWorkState()

    print(n_state.get_state())

    print(n_state.has_change())

    n_state.set_state(1)

    print(n_state.get_state())

    print(n_state.has_change())

    print(n_state.get_state())

    print(n_state.has_change())

    print("Ende")


if __name__ == "__main__":
    main()

