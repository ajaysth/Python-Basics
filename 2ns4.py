# # CREATE A FILR AND STORE DATA USING PYTHON
# f=open("demo.txt","w")
# f.write("I am ajayshrestha and ajay is very nice . ajay is a hero")
# f.close()

#now replace ajay with messi
with open("demo.txt","r") as f:
    data=f.read()
    data2=data.replace("ajay","messi")  
    print(data2)
