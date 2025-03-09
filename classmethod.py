# class Student:
#     name = "Ajay"
     
#     def changeName(self,name):
#         Student.name=name

# s1 = Student()
# s1.changeName("culer")
# print(s1.name)
# print(Student.name)


# class Student:
#     name="Ajay"
#     def changeName(self,name):
#         self.__class__.name=name

# s1 = Student()
# s1.changeName("hero")  
# print(s1.name)   
# print(Student.name)   


# class Student:
#     name="Ajay"

#     @classmethod
#     def changeName(cls,name):
#         cls.name= name

# s1 = Student()
# s1.changeName("Spiderman")
# print(s1.name)
# print(Student.name)



#PROPERTY DECORATOR

class Marks:
    def __init__(self,science,physics,nepali):
        self.science = science
        self.physics = physics
        self.nepali = nepali

    @property
    def Percentage(self):
        return (self.science+self.physics+self.nepali)/3 


m1 = Marks(22,34,23)
print(m1.Percentage)

