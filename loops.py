#two loops in py: 1)while and 2)for

#WHILE LOOP

# i=1
# while(i<=5):
#     print("I am ajay")
#     i+=1
# i=1
# while(i<=10):
#     print("number: ",i)
#     i+=1
# print("Loop ended")


#BREAK AND CONTINUE
# i=1
# while(i<=10):
#     print(i)
#     if(i==4):
#         break
#     i+=1


# j=1
# while(j<=10):
#     if(j==4):
#         j+=1
#         continue
#     else:
#         print(j)
#     j+=1



#FOR LOOP

# el=[3,4,2,33,44]
# for e in el:
#     print(e)


# string="AjayShrestha"
# for el in string:
#     print(el)

# string="AjayShrestha"
# for el in string:
#     if(el=="S"):
#         print("S found")
#         break
# else:
#     print("Ended")    


#RANGE(a sequence of a number):range(start,stop,step)
# for el in range(6,18,3):
#     print(el)
    

#PASS: null statement, used as placeholder for future code
for i in range(3):
    pass
print("Some works done")