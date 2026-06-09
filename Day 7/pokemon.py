class Pokemon:
    def __init__(self,name,level = 1):
        self.name = name
        self.level = level 
        
    def attack(self):
        print("Pokemon",self.name,"is attacking!!")
        
class WaterPokemon(Pokemon): 
    def attack(self): 
        super().attack() #super() is used to call the parent class method 
        print("Water Pokemon",self.name,"is attacking with water!!") 

squirtle = WaterPokemon("Squirtle",5) 
squirtle.attack() 