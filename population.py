from schedule import Schedule


class Population:
    def __init__(self, size, data):
        self.size = size
        self.data = data
        self.schedules = []

    def initialize(self):
        for i in range(0, self.size):
            self.schedules.append(Schedule(self.data).initialize())

    def get_schedules(self):
        return self.schedules
