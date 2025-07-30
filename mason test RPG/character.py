class Character:

    def __init__(self):

        self.name = ""

        # This is for stats
        self.max_hp = 0
        self.current_hp = 0
        self.max_mp = 0
        self.current_mp = 0

        # TODO: should be replaced with a "weapon class" dito for the armor
        # this is strictly stats from equipment
        self.attack_value = 0
        self.defense_value = 0

        # this is for agility, hit chance, doubling, etc...
        self.speed = 0

        self.strength = 0
        self.magic = 0
        self.endurance = 0
        self.agility = 0
        self.luck = 0



    def update_health(self, value):

        self.current_hp += value

        if self.current_hp > self.max_hp:
            self.current_hp = self.max_hp

        if self.current_hp <= 0:
            self.current_hp = 0
