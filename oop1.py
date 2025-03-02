
#class
# class Teacher:
#     name="Ajay"


# #object 
# t1=Teacher()
# print(t1.name)    


# class Bike:
#     color="Red"
#     name="r15"

# b1=Bike()
# print(b1.color)
# print(b1.name)

# b2=Bike()
# print(b2.color)
# print(b2.name)


#constructors
# class Examples:
#     name="Ajay"
#     def __init__(self):
#         print("Creating........")
    
# e1=Examples()


# class Students:
#     def __init__(self,fullName):
#         self.name=fullName
    
#     def welcome(self):
#         print("Hola Culers")

# s1=Students("Ajay")
# print(s1.name)
# s2=Students("Sofi")
# print(s2.name)
        
# s1=Students("Ajay")
# s1.welcome()




#STATIC METHODS

class Teachers:
    @staticmethod
    def PrintName():
        print("I am a teacher")

t1=Teachers()
Teachers.PrintName()