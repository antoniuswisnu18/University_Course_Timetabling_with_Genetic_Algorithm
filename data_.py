import sqlite3
from room import Room
from time_ import Session
from subject import Subject
from course import Course
from instructor import Instructor

conn = sqlite3.connect('uctp.db')


class Data:
    def __init__(self):

        self.rooms = []
        self.times = []
        self.instructors = []
        self.courses = []
        self.subjects = []
        self.number_of_classes = 0

        self.set_rooms()
        self.set_times()
        self.set_instructors()
        self.set_courses()
        self.set_subject()

        self.all_data = {
            'Subjects': {'values': self.subjects,
                         'att_list': self.subjects[0].__dict__.keys()},
            'Courses': {'values': self.courses,
                        'att_list': self.courses[0].__dict__.keys()},
            'Instructors': {'values': self.instructors,
                            'att_list': self.instructors[0].__dict__.keys()},
            'Times': {'values': self.times,
                      'att_list': self.times[0].__dict__.keys()},
            'Rooms': {'values': self.rooms,
                      'att_list': self.rooms[0].__dict__.keys()},
        }

    def set_rooms(self):
        cursor = conn.execute("SELECT * FROM ROOM")
        for row in cursor:
            self.rooms.append(Room(row[0], row[1]))

    def set_times(self):
        cursor = conn.execute("SELECT * FROM TIME")
        for row in cursor:
            self.times.append(Session(row[0], row[1]))

    def set_instructors(self):
        cursor = conn.execute("SELECT * FROM INSTRUCTOR")
        for row in cursor:
            self.instructors.append(Instructor(row[0], row[1]))

    def set_courses(self):
        cursor = conn.execute("SELECT * FROM COURSE")
        for row in cursor:
            self.courses.append(Course(row[0], row[1], row[2]))
            self.number_of_classes += 1

    def set_subject(self):
        cursor = conn.execute("SELECT * FROM SUBJECT")
        for row in cursor:
            self.subjects.append(Subject(row[0], row[1], row[2], row[3]))

    def get_rooms(self):
        return self.rooms

    def get_times(self):
        return self.times

    def get_instructor(self):
        return self.instructors

    def get_courses(self):
        return self.courses

    def get_subject(self):
        return self.subjects

    def get_number_of_classes(self):
        return self.number_of_classes
