from fighter import Fighter
import random


class Pirate(Fighter):
    # def __init__(self,name, speed, dexterity, strength, saying):
    #     Fighter.__init__(self,name, speed, dexterity, strength, saying)

    def special(self,other):
        print(f"{self.name} Yells: Cannon Fire!")
        amount = random.randrange((0+(self.speed//2)),(self.strength * 3)) 
        self.damage(other,amount)
        print("A critical blow!")

    def attack(self,other):
        print(f"{self.name} swings a Cutlass!")
        amount = random.randrange(0,self.strength) 
        self.damage(other,amount)
    
    def magic(self,other):
        print(f"{self.name} sends in his parrot, parrot uses swipe")
        amount = random.randrange(0,(self.dexterity*2))
        self.damage(other, amount)

    def heal(self,other):
        print(f"{self.name} Asks: Anyone else need some rum?")
        amount = random.randrange(5,(self.healthmax//5)) 
        self.restore(amount)
