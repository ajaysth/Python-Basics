#create a class hthat takes name and marks of 3 students and create methods to print the marks

# class Students:
#     def __init__(self,fullname,marks):
#         self.name=fullname
#         self.marks=marks
#     def stuMarks(self):
#         print(self.name,self.marks)

        
    
# s1=Students("Ajay",97)
# s2=Students("Sofi",99)
# s3=Students("Leo",90)

# s1.stuMarks()
# s2.stuMarks()
# s3.stuMarks()


# class Students:
#     def __init__(self,fullname,marks):
#         self.name=fullname
#         self.marks=marks
#     def stuTotalMarks(self):
#         sum=0
#         for val in self.marks:
#             sum=sum+val
#         print(self.name,sum)

        
    
# s1=Students("Ajay",[90,98,97])
# s2=Students("Sofi",[99,99,99])
# s3=Students("Leo",[89,80,90])

# s1.stuTotalMarks()
# s2.stuTotalMarks()
# s3.stuTotalMarks()



# CREATE ACCOUNT CLASS WITH 2 ATTRIBUTES:BALANCE AND ACCOUNT NO,CREATE METHODS FOR DEBIT, CREDIT AND PRINTING THE BALANCE
class Account:
    def __init__(self,balance ,account):
        self.balance=balance
        self.account=account

    def Debit(self,amount):
        self.balance=self.balance-amount
        print("Total amount is: ",self.getBalance())

    def Credit(self,amount):
        self.balance=self.balance+amount
        print("Total amount is: ",self.getBalance())
        
    def getBalance(self):
        return self.balance
    
a1=Account(1000,2345)
a1.Debit(400)
a1.Credit(1000)



