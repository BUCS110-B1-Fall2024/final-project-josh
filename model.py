class Player:
    def __init__(self, name):
        self.name = name
        self.hunger = 100
        self.grade = 100

    def actions(self, action):
        if action == "study":
            self.hunger = max(0, self.hunger - 20)
            self.grade = min(100, self.grade + 30)
        elif action == "eat":
            self.hunger = min(100, self.hunger + 30)
            self.grade = max(0, self.grade - 20)
        elif action == "rest":
            self.hunger = min(100, self.hunger + 20)
            self.grade = max(0, self.grade - 10)
        return not self.icheck()

    def icheck(self):
        if self.hunger <= 0 or self.grade <= 0:
            return True
        return False

class LevelAt:
    def __init__(self):
        self.player = None
        self.current_hour = 0
        self.show_description = True
        self.schedule = [
            {
                "time": "8:00 AM",
                "name": "Math",
                "description": "You have an early morning test in your calc class.",
                "hunger_effect": -20,
                "grade_effect": -10
            },
            {
                "time": "9:00 AM",
                "name": "Gym",
                "description": "The gym is overcrowded, maybe you might get head while exercising.",
                "hunger_effect": 20,
                "grade_effect": -5
            },
            {
                "time": "10:00 AM",
                "name": "Breakfast",
                "description": "You can finally eat!.",
                "hunger_effect": -30,
                "grade_effect": -15
            },
            {
                "time": "11:00 AM",
                "name": "Chemistry",
                "description": "You work in teams, you were able to get into a group with studious peers.",
                "hunger_effect": -10,
                "grade_effect": +20
            },
            {
                "time": "12:00 PM",
                "name": "Lunch",
                "description": "You eat lunch with your friends who are brain rotting!",
                "hunger_effect": 25,
                "grade_effect": -10
            },
            {
                "time": "1:00 PM",
                "name": "Writing",
                "description": "The professor won't stop yapping..",
                "hunger_effect": -25,
                "grade_effect": -25
            },
            {
                "time": "2:00 PM",
                "name": "CS",
                "description": "You have a informational cs lecture but you are getting hungry.",
                "hunger_effect": -20,
                "grade_effect": -30
            },
            {
                "time": "3:00 PM",
                "name": "Dorm",
                "description": "You are finally able to rest after a long day!",
                "hunger_effect": -10,
                "grade_effect": -15
            }
        ]

    def naming(self, name):
        self.player = Player(name)

    def get_lev(self):
        return self.schedule[self.current_hour]

    def ncontd(self):
        current_event = self.schedule[self.current_hour]
        self.player.hunger = max(0, min(100, self.player.hunger + current_event["hunger_effect"]))
        self.player.grade = max(0, min(100, self.player.grade + current_event["grade_effect"]))
        if self.player.icheck():
            return False
        self.current_hour += 1
        self.show_description = True
        return self.current_hour < len(self.schedule)

    def aknldge(self):
        self.show_description = False