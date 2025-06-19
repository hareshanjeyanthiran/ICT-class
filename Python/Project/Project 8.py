Profile = {
    "Name":"Hareshan",
    "Age":12,
    "Grade":8,
    "Nationality":"Srilankan"
}

print(Profile.get("Name"))
print(Profile.get("Age"))
del Profile["Nationality"]
del Profile["Age"]
print(Profile)
Profile["Height"]=130
Profile["Weight"]=46
Profile["Mathsmark"]=98

print(Profile)