from prettytable import PrettyTable


class DisplayControl:
    def __init__(self, data):
        self.data = data

    def print_all_data(self):
        self.print_subject()
        self.print_course()
        self.print_room()
        self.print_time()
        self.print_instructor()

    def print_subject(self):
        subjects = self.data.get_subject()
        subject_table = PrettyTable(["ID", "Name", "Semester", "SKS"])

        for subject in subjects:
            subject_table.add_row([subject.id, subject.name, subject.semester, subject.sks])
        print(subject_table)
        return subject_table.get_html_string()

    def print_course(self):
        courses = self.data.get_courses()
        courses_table = PrettyTable(["ID", "Name", "Number of Students"])

        for course in courses:
            courses_table.add_row([course.id, course.name, course.number_of_students])
        print(courses_table)
        return courses_table.get_html_string()

    def print_room(self):
        rooms = self.data.get_rooms()
        rooms_table = PrettyTable(["ID", "Capacity"])

        for room in rooms:
            rooms_table.add_row([room.id, room.capacity])
        print(rooms_table)
        return rooms_table.get_html_string()

    def print_time(self):
        times = self.data.get_times()
        times_table = PrettyTable(["ID", "Session"])

        for time in times:
            times_table.add_row([time.id, time.session])
        print(times_table)
        return times_table.get_html_string()

    def print_instructor(self):
        instructors = self.data.get_instructor()
        instructor_table = PrettyTable(["ID", "Name"])
        for instructor in instructors:
            instructor_table.add_row([instructor.id, instructor.name])
        print(instructor_table)
        return instructor_table.get_html_string()

    def print_population(self, population):
        pop_table = PrettyTable(["No.", "fitness", "NOC", "classes [course, instructor, session, room]"])
        schedules = population.get_schedules()
        for x in range(0, len(schedules)):
            classes = [str(class_) for class_ in schedules[x].get_classes()]
            pop_table.add_row([str(x), round(schedules[x].get_fitness(), 3), schedules[x].number_of_conflict, classes])
        print(pop_table)
        return pop_table

    def print_schedule(self, schedule):
        print(f"fitness of this schedule : {round(schedule.get_fitness(), 3)}")
        schedule_table = PrettyTable(["Class No.", "Course (Number of Students)", "Room (Capacity)", "Instructor",
                                      "Session"])
        classes = schedule.get_classes()
        for class_ in classes:
            schedule_table.add_row([class_.id, f"{class_.course.name}({class_.course.number_of_students})",
                                    f"{class_.room.id}({class_.room.capacity})", class_.instructor.name,
                                    class_.time_.id])
        print(schedule_table)
        return schedule_table
