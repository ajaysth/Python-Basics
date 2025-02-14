#DICTIONARIES= key value pair

# thisdata= {
#     "name": "Ajay",
#     "college": "Everest",
#     "games":["Football","Efootball","Firifiri"], #list
#     "Jersey numbers":(11.0,10,9,11.9),  #tuple
#     "is_Good": True,
    
# }

# print(thisdata)
# print(type(thisdata))
# print(thisdata["games"])
# thisdata["games"]="cricket"
# thisdata["age"]=22
# print(thisdata)


#NESTED DICTIONARIES
dicts={
    "Name":"Ajay",
    "Marks":{
        "AdvJava":100,
        "NetProg":99,
        "DS":98
    },
    "Interests":["Football","Games","Programming"],
}
# print(dicts["Marks"])
# print(dicts["Marks"]["NetProg"])
# print(len(dicts)) 
# print(list(dicts.keys())) #converts in to list
# print(dicts.get("Interests"))

newdict={"player":"messi","strong":True,}
dicts.update(newdict)
print(dicts)