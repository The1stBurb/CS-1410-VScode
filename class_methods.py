class petStore:
    name="Pet Stupid"
    def __init__(self,idn):
        self.idn=idn
        self.anim=[]
        self.ftPt=None
    def adPt(self,anim):
        assert isinstance(anim,animal)
        self.anim.append(anim)
    def rmPt(self,anim):
        try:
            self.anim.remove(anim)
        except:
            print("No animal here")
        else:
            print(anim,"removed")
    def ft(self,nm):
        for pet in self.anim:
            if pet.nm==nm:
                self.ftPt=pet
                print("Featured pet!",pet)
                break
        else:
            print("thats not a pet")
    def gtFt(self):
        return self.ftPt
    def feed(self):
        for i in self.anim:
            i.eat()
    def gtMam(self):
        return self.gbt(mammal)
    def gtRep(self):
        return self.gbt(reptile)
    def gbt(self,typ):
        return [i for i in self.anim if isinstance(i,typ)]
class animal:
    def __init__(self,name):
        self.nm=name
    def __str__(self):
        return f"this is {self.nm}"
    def eat(self):
        print(self.nm,"is eating",self.diet)
class mammal(animal):
    pass
class cat(mammal):
    def __init__(self,name,diet):
        super().__init__(name)
        self.diet=diet
    # diet="mic"
class dog(mammal):
    diet="kibble"
class reptile(animal):
    pass
class snake(reptile):
    diet="rodents"
class turtle(reptile):
    diet="carrots"
class bird(animal):
    pass
class parKeet(bird):
    diet="snake"
class t2can(bird):
    diet="dog"
class rabit:
    pass
store=petStore(1)
store.adPt(turtle("bob"))
store.adPt(cat("jon","mice"))
store.adPt(turtle("dahsr"))
store.adPt(t2can("cat"))
store.ft("dahsr")
store.feed()
store.gtRep()