#DICTIONARIES= key value pair

thisdata= {
    "name": "Ajay",
    "college": "Everest",
    "games":["Football","Efootball","Firifiri"], #list
    "Jersey numbers":(11.0,10,9,11.9),  #tuple
    "is_Good": True,
    
}

# print(thisdata)
# print(type(thisdata))
print(thisdata["games"])
thisdata["games"]="cricket"
thisdata["age"]=22
print(thisdata)


