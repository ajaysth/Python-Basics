#input 3 floating point numbers and print their averages
# num1=float(input("Enter first float number: "))
# num2=float(input("Enter second float number: "))
# num3=float(input("Enter third float number: "))
# avg=(num1+num2+num3)/3
# print(avg)


#INPUT USERS FIRST NAME AND PRINT ITS LENGTH
# name="Ajaaay"
# print(len(name))
# print(name.count("a"))


#check whether input number is odd or even
# num=int(input("enter a number: "))
# if(num % 2==0):
#     print("The number is even")
# else:
#     print("The number is odd")


#FIND GREATEST NUMBER BETWEEN 3 NUMBERS
# number1=int(input("Enter first number: "))
# number2=int(input("Enter second number: "))
# number3=int(input("Enter third number: "))
# if(number1>number2 and number1>number3 ):
#     print("The greatest number is: ", number1)
# elif(number2>number1 and number2>number3):
#     print("The greatest number is ", number2)
# else:
#     print("The greatest number is ", number3)    


#CHECK WHETHER GIVEN HUMBER IS MULTIPLE OF 7 OR NOT
# number=int(input("Enter a number: "))
# if(number % 7 == 0):
#     print("The number is divisible by 7")
# else:
#     print("The number is not divisible by 7")



#INPUT 3 NUMBERS AND STORE THEM IN A LIST
# value1=input("Enter first value: ")
# value2=input("Enter second value: ")
# value3=input("Enter third value: ")
# list=[value1,value2,value3]
# print(list)

#alternative
# list2=[]
# movie1=input("Enter first movie: ")
# movie2= input("Enter second movie: ")
# movie3= input("Enter third movie: ")
# list2.append(movie1)
# list2.append(movie2)
# list2.append(movie3)
# print(list2)



#CHECK WHETHER THE GIVEN LIST IS PALINDROME OR NOT
# list1=[1,2,3,2,1]
# copy_list=list1.copy()
# copy_list.reverse()
# if(list1==copy_list):
#     print("The list is palindrome")
# else:
#     print("Not palindrome")

# list2=[1,2,3]
# copy_list2=list2.copy()
# copy_list2.reverse()
# if(list2==copy_list2):
#     print("The list is palindrome")
# else:
#     print("Not palindrome")

#   WAP A PROGRAM TO COUNT THE STUDENT HAVING GRADE "A" IN TUPLE
# tup=("A","B","A","E","B","A","A","C")
# res=tup.count("A")
# print("The number of students having grade is: ",res)



#WRITE ABOVE TUPLE IN LIST AND SORT THEM FROM A TO D
# list=["A","B","A","E","B","A","A","C"]
# list.sort()
# print(list)



#STORE THE VALUES IN THE DICTIONARIES

# dict={
#     "cat":"an animal",
#     "table":["a piece of furniture","list of facts and figures"],
#     1911:("the lucky number","most special number")
# }
# print(dict)

#QN
# subjects={"python","c","java","python","c++","python"}  #set
# print(len(subjects))

#CREATE AN EMPTY DICTIONARY AND ADD UPTO 3 SUBJECTS WITH MARKS ONE BY ONE
# marks={}
# sub1={"DS":99}
# sub2={"OS":100}
# sub3={"DSA":98}
# marks.update(sub1)
# print(marks)
# marks.update(sub2)
# print(marks)
# marks.update(sub3)
# print(marks)

#now from user inputs
# marks2={} #dictionary
# print(type(marks2))
# sub1=int(input("Enter marks for OS: "))
# marks2.update({"OS":sub1})
# print(marks2)
# sub2=int(input("Enter marks for DSA: "))
# marks2.update({"DSA":sub2})
# print(marks2)
# sub3=int(input("Enter marks for OS: "))
# marks2.update({"Java":sub3})
# print(marks2)


#STORE 9 AND 9.0 IN THE SAME SET
# collection={9,9.0}
# print(type(collection))
# collection2={
#     ("float",9.0),
#     ("int",9)
# }
# print(collection2)





