class Course:
    def __init__(self, id, name, number_of_students):
        self.id = id
        self.name = name
        self.number_of_students = number_of_students

    def get_course_name(self):
        return str(self.name)
