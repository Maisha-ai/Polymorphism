# class cat():
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def info(self):
#         print("I am a Cat and my name is",self.name,"and my age is", self.age)
#     def makesound(self):
#         print("Meow")

# class dog():
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def info(self):
#         print("I am a Dog and my name is",self.name,"and my age is", self.age)
#     def makesound(self):
#         print("Bark")

# Cat= cat("Oreo",6)
# Dog=dog("Gray",8)

# for animal in (Cat,Dog):
#     animal.info()
#     animal.makesound()

# Activity 2

class computer:
    def __init__(self):
        self.__maxprice=900
    def sell(self):
        print("Selling price is", self.__maxprice)
    def set_maxprice(self,price):
        self.__maxprice=price

C=computer()
C.sell()
C.__maxprice=1000
C.sell()
C.set_maxprice(1000)
C.sell()