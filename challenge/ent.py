from fighter import Fighter
import random

class Treant(Fighter):
    # def __init__(self,name, speed, dexterity, strength, saying):
    #     Fighter.__init__(self,name, speed, dexterity, strength, saying)

    def special(self,other):
        print(f"{self.name} grows a treestar")
        self.restore(self.healthmax-self.health) 
        return self

    def attack(self,other):
        print(f"{self.name} swings a branch")
        amount = random.randrange(0,self.strength) 
        self.damage(other,amount)
    
    def magic(self,other):
        print(f"{self.name} is sending the roots")
        amount = random.randrange(0,self.dexterity) 
        self.damage(other, amount)

    def heal(self,other):
        print(f"{self.name}'s limbs are regenerating")
        amount = random.randrange(5,15) 
        self.restore(amount)



