
# bonus modularization inheritance
# parent class
class Fighter:
    def __init__(self, name, speed, dexterity, strength, health, saying):
        self.name = name
        self.speed = speed
        self.strength = strength
        self.dexterity = dexterity
        self.saying = saying
        self.health = health
        self.healthmax = health

    def greeting(self):
        print(f"Hello my name is {self.name}. {self.saying}")
        return self

    def check_health(self):
        if self.health <= 0:
            print(f"{self.name} I am Defeated")
        return not self.health <= 0

    def displayHealth(self):
        print(f"{self.name}'s health: {self.health}")
        return self

    def damage(self, other, amount):
        dmg = amount
        other.health -= dmg
        print(f"{self.name} hit {other.name} for {dmg} damage")
        other.displayHealth()
        return self

    def restore(self, amount):
        self.health += amount
        print(f"{self.name} healed {amount}")
        return self

    def displayInfo(self):
        print(f"\nName: {self.name}\nYour Characters Stats are:\nSpeed: {self.speed}\nDexterity: {self.dexterity}\nStrength: {self.strength}\nHealth: {self.health}\nYour Saying is: {self.saying}\n")
        return self
