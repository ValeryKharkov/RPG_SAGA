class Hero:
    def __init__(self, first_name, last_name, health_points, attack_points):
        self.first_name = first_name
        self.last_name = last_name
        self.health_points = health_points
        self.attack_points = attack_points

    pass


class Knight(Hero):
    def nemesis (self):
        self.attack_points = self.attack_points + (self.attack_points * 30) / 100
    pass


class Archer(Hero):
    def fire_arrows(self):
        self.health_points = self.health_points - 2
    pass


class Wizard(Hero):
    def bewitchment(self):
        ...
    pass


