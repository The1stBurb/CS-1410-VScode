from random import randint
#PascalCase or CamelCase
class Animal:
    def __init__(self,name,species,age,gender,rarity):
        self.name,self.species,self.age,self.gender,self.rarity=name,species,age,gender,rarity
        self.fights={"won":0,"tie":0,"lost":0}
    def get_name(self):
        return self.name
    def __str__(self):
        return f"Name: {self.name}\nSpecies: {self.species}\nAge: {self.age}\nGender: {self.gender}\nRarity: {self.rarity}\nWins: {self.fights["won"]}\nTies: {self.fights["tie"]}\nLosses: {self.fights["lost"]}\n"
    def fight(self,other):
        sl,ol=len(self.name+self.species+str(self.age)+self.gender+self.rarity),len(other.name+other.species+str(other.age)+other.gender+other.rarity)
        sl+=randint(-round(sl/5),round(sl/5))
        ol+=randint(-round(ol/5),round(ol/5))
        wnr="No one"
        if sl>ol:
            wnr=self.name
            self.fights["won"]+=1
            other.fights["lost"]+=1
        elif ol>sl:
            wnr=other.name
            other.fights["won"]+=1
            self.fights["lost"]+=1
        else:
            self.fights["tie"]+=1
            other.fights["tie"]+=1
        return f"{wnr} wins!\n# of wins of {self.name} is {self.fights["won"]}\n# of wins of {other.name} is {other.fights["won"]}\n"
# cat=Animal("Cat","Cat",2315,"guy","almost extinct")
# dog=Animal("dog","dog",21354,"guys","very extincted")
# print(cat)
# print(dog)
# print(cat.fight(dog))
# cat.name="Cattus"
# print(cat.fight(dog))