class Room:
    def __init__(self, id, capacity):
        self.id = id
        self.capacity = capacity

    def get_id(self):
        return str(self.id)
