class Subject:
    def __init__(self, id, name, semester, sks):
        self.id = id
        self.name = name
        self.semester = semester
        self.sks = sks

    def get_subject_name(self):
        return str(self.name)
