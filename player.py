class Player:
    def __init__(self, name, hunger=100, grade=100, img_file=None):
        
        self.name = name
        self.hunger = hunger
        self.grade = grade
        self.img_file = img_file

    def take_action(self, action):
        
        if action == "network":
            self.hunger = max(0, self.hunger - 10)
            self.grade = min(100, self.grade + 20)

        elif action == "study":
            self.hunger = max(0, self.hunger - 20)
            self.grade = min(100, self.grade + 30)

        elif action == "rest":
            self.hunger = min(100, self.hunger + 20)
            self.grade = max(0, self.grade - 10)

        elif action == "eat":
            self.hunger = min(100, self.hunger + 30)
            self.grade = max(0, self.grade - 20)
            
        elif action == "procrastinate":
            self.hunger = min(100, self.hunger + 40)
            self.grade = max(0, self.grade - 40)

    def is_alive(self):
        
        return self.hunger > 0 and self.grade > 0
