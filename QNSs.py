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
tup=(2,5,1,55,3,2,3,11,55,9) #find 3
i=0
x=9
while(i<len(tup)):
    if(tup[i]==x):
        print("Found at index: ",i)
    i+=1    

        