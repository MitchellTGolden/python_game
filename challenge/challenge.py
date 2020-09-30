#Possible classes to battle
    #Alien
        #blue alien
        #red alien
    #Robot
    #Ninja
    #Cowboys
    #Pirates
    #Dinosaurs
#Possible methods to have
#Attack(general attack)
#Special weapon
#heal
#magic
#defend

#bonus modularization inheritance
#parent class
class Fighter:
    def __init__(self,name, speed, dexterity, strength, health, saying):
        self.name = name
        self.speed = speed
        self.strength= strength 
        self.dexterity= dexterity
        self.saying = saying
        self.health = health
    def greeting(self):
        print(f"Hello my name is {self.name}. {self.saying}")
        return self

    def check_health(self):
        if self.health <=0:
            print(f"{self.name} I am Defeated")
        return not self.health <=0

    def displayHealth(self):
        print(f"Name:{self.name} Health: {self.health}")
        return self

    def damage(self, other):
        dmg = self.strength
        other.health -= dmg
        print(f"{self.name} hit {other.name} for {dmg} damage")
        other.displayHealth()
        return self 

    def heal(self,amount):
        self.health += amount
        print(f"{self.name} healed {amount}")
        return self


    # def tornado_kick(self, other_ninja):



class Robot(Fighter):
    # def __init__(self,name, speed, dexterity, strength, saying):
    #     Fighter.__init__(self,name, speed, dexterity, strength, saying)

    def special(self,amount):
        print("I'll fix it!")
        self.heal(amount)
        return self
    

bender = Robot('Bender', 10, 5, 10, 50, "Hey")#.greeting().displayHealth().special(10).displayHealth()
walle = Robot('Walle', 10, 5, 10, 50, "Walllllll EEEE")#.greeting().displayHealth()

walle.damage(bender)

class Ninja(Fighter):
    # def __init__(self,name, speed, dexterity, strength, saying):
    #     Fighter.__init__(self,name, speed, dexterity, strength, saying)

    def special(self,amount):
        print("I got caught off guard, need to heal.")
        self.heal(amount)
        return self
    