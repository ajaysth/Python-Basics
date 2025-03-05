#DEL keyword

# class Teacher:
#     def __init__(self,name):
#         self.name=name

# t1=Teacher("Ajay")
# print(t1.name)
# del t1
# print(t1.name)


# PRIVATE ATTRIBUTES

# class Account:
#     def __init__(self,acc_no,acc_pw):
#         self.acc_no = acc_no
#         self.__acc_pw=acc_pw

#     def reser_pw(self):
#         print(self.__acc_pw)

# a1= Account("123","abcd")
# print(a1.acc_no)
# a1.reser_pw()       

# class Student:
#     __name="Ajay"

#     def __printName(self):
#      print("Hello users")

#     def hello(self):
#      self.__printName()


# s1 = Student()
# s1.hello()
# print(s1.__name)
# s1.__printName()