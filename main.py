from models.team import Team
from models.coach import Coach
from gui import FootballManagerGUI

def main():
    team = Team("Dream FC")
    coach = Coach("Ruben Amorim", 40, 10)
    app = FootballManagerGUI(team, coach)
    app.root.mainloop()

if __name__ == "__main__":
    main()
