from fighter import Fighter
import random

class Robot(Fighter):

    def special(self,other):
        print(f"{self.name} Yells: 10101001001")
        amount = random.randrange((0+(self.speed//2)),(self.strength * 3)) 
        self.damage(other,amount)
        print("010101")

    def attack(self,other):
        print("0.0!")
        amount = random.randrange(1,self.strength) 
        self.damage(other,amount)
    
    def magic(self,other):
        print("....Loading")
        amount = random.randrange(0,self.dexterity) 
        self.damage(other, amount)

    def heal(self,other):
        print(f"{self.name} is initiating repairs")
        amount = random.randrange(5,15) 
        self.restore(amount)
