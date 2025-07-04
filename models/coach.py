from .person import FootballPerson

class Coach(FootballPerson):
    def __init__(self, name, age, experience_years):
        super().__init__(name, age)
        self.experience = experience_years

    def get_role_info(self):
        return f"👤 Coach: {self.name}"
