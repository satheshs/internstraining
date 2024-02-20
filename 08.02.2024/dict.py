#contact  list

contactList={}

contactList["Person1"]={"id":1234,
    "name":"Dhina",
    "email":"dhina0508@gmail.com",
    "phone":9384300417
}

contactList["Person2"]={"id":1234,
    "name":"Deepak",
    "email":"deepak@gmail.com",
    "phone":9876543234
}

contactList["Person3"]={"id":1234,
    "name":"Ram",
    "email":"ram@gmail.com",
    "phone":9567854678
}
print(contactList)




#update contact information

for i in range(len(contactList)):
    if contactList["Person"+str(i+1)]["id"]==1236:
        contactList["Person"+str(i+1)]["email"]="ramkumar@gmail.com"
        
print(contactList)



#check for key

name=str(input())
answer=False
for i in range(len(contactList)):
    if contactList["Person"+str(i+1)]["name"]==name:
        print(contactList["Person"+str(i+1)])
        answer=True
        break

if answer==False:
    print("User not Found")


#Iterate and Display

for i in range(len(contactList)):
    print("Name:",contactList["Person"+str(i+1)]["name"])
    print("Phone Number:",contactList["Person"+str(i+1)]["phone"],"\n")


#Adding a New Contact

name=input("Enter name: ")
email=input("Enter email: ")
phone=input("Enter phone: ")

for i in range(len(contactList)+1,len(contactList)+2):
    contactList["person"+str(i)]={
    "id":1235+i,
    "name":name,
    "email":email,
    "phone":phone}
print(contactList)


#removing a contact
remove = 'Person3'
if remove in contactList:
    del contactList[remove]
print(contactList)


#combine dictionaries
additionalContactList={}

additionalContactList["Person4"]={"id":1245,
    "name":"Ramesh",
    "email":"ramesh0508@gmail.com",
    "phone":9384890987
}

additionalContactList["Person5"]={"id":1246,
    "name":"Suresh",
    "email":"suresh@gmail.com",
    "phone":9876540987
}

contactList.update(additionalContactList)
print(contactList)




#sorting key
sorted_list = dict(sorted(contactList.items()))
print(sorted_list)




#nested dictionary
contactList["Person6"]={"id":1236,
    "name":"Ram",
    "email":"ram@gmail.com",
    "phone":9567854678,
    "personal_info":{
        "DOB":"21/03/2002",
        "age":30
    },
    "work_info":{
        "position":"Full Stack",
        "Experience":"5 years"
    }
}

print(contactList)



