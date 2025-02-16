#PRINT THE LENGTH OF THE LISTS
# heroes=["spiderman","superman","batman"]
# players=["Messi","penaldo","Neymar","Suarez"]

# def print_len(list):
#     print(len(list))

# print_len(players)    
# print_len(heroes)


#PRINT ELEMEM=NTS OF A LISTS IN SAME LINE USING FUNCTION
# heroes=["spiderman","superman","batman"]
# players=["Messi","penaldo","Neymar","Suarez"]

# def printSameLine(list):
#     print(list)

# printSameLine(players)            
# printSameLine(heroes)



# heroes=["spiderman","superman","batman"]
# players=["Messi","penaldo","Neymar","Suarez"]

# def printSameLine(list):
#     for el in list:
#         print(el, end=" ")

# printSameLine(heroes)



#FIND THE FACTORIAL OF N
# def Factorial(number):
#     fact=1
#     for i in range(1,number+1):
#         fact=fact*i
#     print(fact)

# Factorial(5)  #using for

   #using while
def Factorial(number):
    fact=1
    i=1
    while(i<=number):
        fact=fact*i
        i+=1
    print(fact)

Factorial(5)    