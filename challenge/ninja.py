from fighter import Fighter
import random


class Ninja(Fighter):
    # def __init__(self,name, speed, dexterity, strength, saying):
    #     Fighter.__init__(self,name, speed, dexterity, strength, saying)
    def special(self, other):
        print(f"{self.name} Yells: *ninja sound*")
        amount = random.randrange((0+(self.speed)), (self.strength*2))
        self.damage(other, amount)
        print("ninja ")

    def heal(self, other):
        print("I must recover!")
        amount = random.randrange(5, 15)
        self.restore(amount)
        print(f"{self.name} healed for: {amount}")

    def attack(self, other):
        print("Ninja star!")
        amount = random.randrange(1, self.strength)
        self.damage(other, amount)

    def magic(self, other):
        print(f"{self.name}: Feel the power of my jutsu!")
        amount = random.randrange(0, self.speed)
        self.damage(other, amount)


# if __name__ == "__main__":
#     # .greeting().displayHealth().special(10).displayHealth()
#     psychomantis = Ninja('Psychomantis', 10, 10, 5, 50, "I'm that ninja")
#     # .greeting().displayHealth()
#     naruto = Ninja('Naruto', 10, 5, 10, 50, "Believe it")
#     psychomantis.damage(naruto)

#     #     def special(self,other):
#     #     print(f"{self.name} Yells: 10101001001")
#     #     amount = random.randrange((0+(self.speed/2)),(self.strength * 3))
#     #     self.damage(other,amount)
#     #     print("010101")

#     # def attack(self,other):
#     #     print("0.0!")
#     #     amount = random.randrange(1,self.strength)
#     #     self.damage(other,amount)

#     # def magic(self,other):
#     #     print("....Loading")
#     #     amount = random.randrange(0,self.dexterity)
#     #     self.damage(other, amount)

#     # def heal(self,other):
#     #     print(f"{self.name} is initiating repairs")
#     #     amount = random.randrange(5,15)
#     #     self.heal(amount)
#     #     print(f"{self.name} healed for :{amount}")
