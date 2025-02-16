#print from 1 to 100
# i=1
# while(i<=100):
#     print(i)
#     i+=1

#PRINT MULTIPLE OF 7
# i=1
# while(i<=10):
#     print("7 * ",i,": ", 7*i)
#     i+=1

#PRINT [1,4,9,16,25,36,49,64,81,100] USING LOOP
# list1=[]
# index=0
# i=1
# while(index<=9):
#     print(i*i)
#     index+=1
#     i+=1

#alternatives
# output=[]
# i=1
# while(i<=10):
#     output.append(i*i)
#     i+=1
# print(output)    

#SEARCH FOR  NUMBER IN A TUPLE USING LOOP
# tup=(2,5,1,55,3,2,3,11,55,9) #find 3
# i=0
# x=9
# while(i<len(tup)):
#     if(tup[i]==x):
#         print("Found at index: ",i)
#     i+=1    


#SEARCH FOR NUMBER X ON THE LIST
# list=[2,3,5,1,7,22,43,54,99]
# index=0
# for el in list:
#     if(el==43):
#         print("Number found at index: ",index)
#     index+=1    
    

#PRINT NUMBER FROM 1 TO 100 USING FOR AND RANGE
# for i in range(101):
#     print(i)
        

#PRINT NUMBER FROM 1 TO 100 USING FOR AND RANGE
# for el in range(100,2,-1):
#     print(el)

#PRINT multiple od n  USING FOR AND RANGE
# num=int(input("Enter the number u want to print the table of: "))
# for i in range(1,11,1):
#     print(num,"*",i,"=",num*i)


#PRINT SUM OF FORST N NATURAN NUMBERS(using while)
# num=int(input("Enter the number: "))
# i=0
# sum=0
# while(i<=num):
#     sum=sum+i
#     i+=1
# print(sum)


#FIND THE FACTORIAL OF N(use for)

num=int(input("Enter the number: "))
fact=1
for i in range(1,num+1):
    fact=fact*i
print(fact)
