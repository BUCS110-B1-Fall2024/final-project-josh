class State:
    
    def __init__(self, players):
        
        self.checkpoints = [
            "8AM Class with Test", "9AM Gym Session", "10AM Brunch",
            "11AM Science Lab", "12PM Lunch", "1PM Writing Class",
            "2PM CS Class", "3PM Return to Dorm"
        ]
        self.players = players
        self.current_checkpoint = 0

    def advance_checkpoint(self):
        
        if self.current_checkpoint < len(self.checkpoints) - 1:
            self.current_checkpoint += 1

    def get_checkpoint(self):
        
        return self.checkpoints[self.current_checkpoint]
