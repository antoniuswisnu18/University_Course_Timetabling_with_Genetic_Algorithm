class Session:
    def __init__(self, id, session):
        self.id = id
        self.session = session

    def get_time_id(self):
        return str(self.id)
