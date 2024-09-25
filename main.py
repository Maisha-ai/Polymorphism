class cat():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print("I am a Cat and my name is",self.name,"and my age is", self.age)
    def makesound(self):
        print("Meow")

class dog():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print("I am a Dog and my name is",self.name,"and my age is", self.age)
    def makesound(self):
        print("Bark")

Cat= cat("Oreo",6)
Dog=dog("Gray",8)

for animal in (Cat,Dog):
    animal.info()
    animal.makesound()