# def CalcSum():
#     print(2+3)
  
# CalcSum  ()

# def CalcMul(x,y):
#     mul=x*y
#     print(mul)

# CalcMul(3,3)

# def AvgCalc():
#     a=3
#     b=9
#     c=12
#     avg=(a+b+c)/3
#     return avg

# res=AvgCalc()
# print(res)



#RECURSIONS
# def show(n):
#     if(n==0):
#         return
#     print(n)
#     show(n-1)
# show(7)

#FACTORIAL USING RECURSION
# def Factorial(n):
#     if(n==0 or n==1):
#         return 1
#     else:
#         return n*Factorial(n-1)

# res=Factorial(5)
# print(res)


#PRINT ALL NUMBER IN THE LIST USING RECURSIVE FUNCTION
hero=["Ajay","Shrestha","Messi","Hehe"]
def Example(list,index):
    if(index==len(hero)):
        return
    print(list[index])
    Example(list,index+1)
Example(hero,0)    