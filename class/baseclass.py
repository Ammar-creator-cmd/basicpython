class footballer:
    def __init__(self, name, age, team):
        self.name = name
        self.age = age
        self.team = team
    def info(self):
        print(f"{self.name} is {self.age} years old and plays for {self.team}.")
    def play(self):
        print(f"{self.name} is playing for {self.team}.")
    def score(self):
        print(f"{self.name} has scored a goal for {self.team}.")
class midfielder(footballer):
    def __init__(self, name, age, team, position):
        super().__init__(name, age, team)
        self.position = position
    def play(self):
        print(f"{self.name} is playing as a {self.position} for {self.team}.")

class defender(footballer):
    def __init__(self, name, age, team, position):
        super().__init__(name, age, team)
        self.position = position
    def play(self):
        print(f"{self.name} is playing as a {self.position} for {self.team}.")
    def tackle(self):
        print(f"{self.name} has made a tackle for {self.team}.")
class forward(footballer):
    def __init__(self, name, age, team, position):
        super().__init__(name, age, team)
        self.position = position
    def play(self):
        print(f"{self.name} is playing as a {self.position} for {self.team}.")

class goalkeeper(footballer):
    def __init__(self, name, age, team, position):
        super().__init__(name, age, team)
        self.position = position
    def play(self):
        print(f"{self.name} is playing as a {self.position} for {self.team}.")
    def save(self):
        print(f"{self.name} has made a save for {self.team}.")
class winger(footballer):
    def __init__(self, name, age, team, position):
        super().__init__(name, age, team)
        self.position = position
    def play(self):
        print(f"{self.name} is playing as a {self.position} for {self.team}.")

class coach(footballer):
    def __init__(self, name, age, team, role):
        super().__init__(name, age, team)
        self.role = role
    def info(self):
        print(f"{self.name} is {self.age} years old and is the {self.role} of {self.team}.")
    def play(self):
        print(f"{self.name} is coaching {self.team}.")

player1 = midfielder("Declan Rice", 24, "Arsenal", "Central Midfielder")
player1.info()
player1.play()
player1.score()

player2 = defender("William Saliba", 22, "Arsenal", "Centre Back")
player2.info()
player2.play()
player2.tackle()

player3 = forward("Kai Havertz", 24, "Arsenal", "Striker")
player3.info()
player3.play()
player3.score()

player4 = goalkeeper("David Raya", 28, "Arsenal", "Goalkeeper")
player4.info()
player4.play()
player4.save()

player5 = winger("Bukayo Saka", 22, "Arsenal", "Right Winger")
player5.info()
player5.play()
player5.score()

player6 = coach("Mikel Arteta", 41, "Arsenal", "Head Coach")
player6.info()
player6.play()
