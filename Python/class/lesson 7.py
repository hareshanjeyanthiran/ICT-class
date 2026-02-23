Profile = {
    "Name":"Hareshan",
    "Age":12,
    "Grade":8,
    "Nationality":"Srilankan"
}

SmartPhone = {
    "Brand":"OnePlus" ,
    "RAM":8 ,
    "ROM":128 ,
    "Display": "AMOLED" ,
    "Battery":"Li-on"
}


#Accessing element
print(Profile.get("Name"))
print(Profile.get("Age"))
print(SmartPhone.get("Brand"))

print(SmartPhone["Display"])
print(SmartPhone["Battery"])

#Updating data

SmartPhone["RAM"] = 10
SmartPhone["Display"] = "OLED"
print(SmartPhone)

#Deleting an element

del Profile["Nationality"]
del Profile["Age"]
print(Profile)

#add data

Profile["Height"]=130
Profile["Weight"]=46
Profile["Mathsmark"]=98

print(Profile)