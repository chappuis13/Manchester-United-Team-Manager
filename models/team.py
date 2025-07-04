from .player import Player
import json

class Team:
    def __init__(self, name):
        self.name = name
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def list_players(self):
        return [p.get_role_info() for p in self.players]

    def save_to_file(self, filepath):
        data = []
        for p in self.players:
            data.append({
                "name": p.name,
                "age": p.age,
                "position": p.position,
            })
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=2)

    def load_from_file(self, filepath):
        with open(filepath, 'r') as f:
            data = json.load(f)
        self.players = []
        for item in data:
            p = Player(item["name"], item["age"], item["position"])
            self.players.append(p)
