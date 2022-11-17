class Class:
    def __init__(self, class_numb, course):
        self.id = class_numb
        self.course = course
        self.instructor = None
        self.time_ = None
        self.room = None

    def set_instructor(self, instructor):
        self.instructor = instructor

    def set_time(self, time):
        self.time_ = time

    def set_room(self, room):
        self.room = room

    def get_id(self):
        return self.id

    def get_course(self):
        return self.course

    def get_instructor(self):
        return self.instructor

    def get_time(self):
        return self.time_

    def get_room(self):
        return self.room

    def __str__(self):
        return str(self.course.id) + ",I" + str(self.instructor.id) + "," + \
               str(self.time_.id) + "," + str(self.room.id)

