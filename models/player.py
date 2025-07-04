from .person import FootballPerson

class Player(FootballPerson):
    def __init__(self, name, age, position):
        super().__init__(name, age)
        self.position = position

    def get_role_info(self):
        return f"Player: {self.name} – {self.position}"
