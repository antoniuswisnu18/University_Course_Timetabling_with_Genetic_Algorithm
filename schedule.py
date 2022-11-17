from class_ import Class
from random import randrange


class Schedule:
    def __init__(self, data):
        self.data = data
        self.classes = []
        self.number_of_classes = 0
        self.number_of_conflict = 0
        self.fitness = -1
        self.is_fitness_changed = True

    def initialize(self):
        courses = self.data.get_courses()
        for x in range(0, len(courses)):
            new_class = Class(self.number_of_classes, courses[x])
            self.number_of_classes += 1
            new_class.set_room(self.data.get_rooms()[randrange(len(self.data.get_rooms()))])
            new_class.set_time(self.data.get_times()[randrange(len(self.data.get_times()))])
            new_class.set_instructor(self.data.get_instructor()[randrange(len(self.data.get_instructor()))])
            self.classes.append(new_class)
        return self

    def calculate_fitness(self):
        self.number_of_conflict = 0
        for x in range(0, self.number_of_classes):
            if self.classes[x].room.capacity < self.classes[x].course.number_of_students:
                self.number_of_conflict += 1
                # print(self.number_of_conflict)
                # print(x)

            for y in range(0, self.number_of_classes):
                if y >= x:
                    if self.classes[x].time_.id == self.classes[y].time_.id and self.classes[x].id != self.classes[y].id:
                        if self.classes[x].room.id == self.classes[y].room.id:
                            self.number_of_conflict += 1
                            # print(self.number_of_conflict)
                            # print(x, y)

                        if self.classes[x].instructor.id == self.classes[y].instructor.id:
                            self.number_of_conflict += 1
                            # print(self.number_of_conflict)
                            # print(x, y)

        return 1 / ((float(self.number_of_conflict)) + 1)

    def get_classes(self):
        self.is_fitness_changed = True
        return self.classes

    def get_number_of_conflict(self):
        return self.number_of_conflict

    def get_fitness(self):
        if self.is_fitness_changed:
            self.fitness = self.calculate_fitness()
        self.is_fitness_changed = False
        return self.fitness

