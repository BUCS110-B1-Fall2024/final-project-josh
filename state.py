import random

class State:
    def __init__(self, players):
        self.players = players
        self.checkpoints = [
            {
                "name": "8AM Class with Test",
            },
            {
                "name": "9AM Gym",
                
            },
            {
                "name": "10AM Breakfast",
                
            },
            {
                "name": "11AM Science Lab",
                
            },
            {
                "name": "12PM Lunch",
                
            },
            {
                "name": "1PM Writing Class",
                
            },
            {
                "name": "2PM CS Class",
                
            },
            {
                "name": "3PM Return to Dorm",
                
            }
        ]
        self.current_checkpoint = 0

    def current_level(self):
        return self.checkpoints[self.current_checkpoint]

    def level_damage(self):
        checkpoint = self.current_level()["name"]
        for player in self.players:
            if checkpoint == "8AM Class with Test":
                player.hunger = max(0, player.hunger - 20)
                if random.randint(0, 1) == 0:
                    player.grade = min(100, player.grade + 20)
                else:
                    player.grade = max(0, player.grade - 20)
            elif checkpoint == "9AM Gym Session":
                player.hunger = max(0, player.hunger - 20)
                if random.randint(1, 5) == 1:
                    player.grade = max(0, player.grade - 20)
                    player.hunger = max(0, player.hunger - 20)
            elif checkpoint == "10AM Brunch":
                player.hunger = min(100, player.hunger + 30)
            elif checkpoint == "11AM Science Lab":
                player.grade = min(100, player.grade + 20)
            elif checkpoint == "12PM Lunch":
                player.hunger = min(100, player.hunger + 20)
                if random.randint(0, 1) == 0:
                    player.grade = max(0, player.grade - 20)
            elif checkpoint == "1PM Writing Class":
                player.hunger = max(0, player.hunger - 20)
                player.grade = max(0, player.grade - 20)
            elif checkpoint == "2PM CS Class":
                player.grade = min(100, player.grade + 30)
                player.hunger = max(0, player.hunger - 10)