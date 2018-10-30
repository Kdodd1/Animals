class animals:
    def __init__(self, name):
        self.name = name
        self.health = 100
    
    def walk(self):
        self.health -= 5
        return self
    
    def run(self):
        self.health -= 10
        return self
    
    def displayHealth(self):
        print("Health: " + str(self.health))

#Child of Animal Class    
class dog(animals):
    def __init__(self, name):
        super().__init__(name)
        self.name = name
        self.health = 170
        
    def pet(self):
        self.health += 5
        return self

#Child of Animal Class
class dragon(animals):
    def __init__(self, name):
        super().__init__(name)
        self.name = name
        self.health = 170
        
    def fly(self):
        self.health -= 10
        return self
        
    def displayHealth(self):
        super().displayHealth()
        print("I am a dragon")
        
#Child of Animal Class
class tiger(animals):
    def __init_(self, name):
        super().__init__(name)
        self.name = name
        self.health = 150
        
    def run(self):
        super().run()
        print("I am really fast")
        self.health += 20
        return self

##Example output
smaug = dragon("Smaug")
cliffard = dog("Cliff")
tony = tiger("Tony the Tiger")

cliffard.walk().pet().displayHealth()
smaug.walk().fly().displayHealth()
tony.run().displayHealth()
