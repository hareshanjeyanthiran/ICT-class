# Friends
Myfile = open("Friends.txt", "w")
Myfile.write("Hareshan\n")
Myfile.write("Jileshan\n")
Myfile.write("Kartik\n")
Myfile.write("Gab\n")
Myfile.close()

#Adding more friends
Myfile = open("Friends.txt", "a")
Myfile.write("Rinu\n")
Myfile.write("Ram\n")
Myfile.close()

# Reading the file
Myfile = open("Friends.txt", "r")
content = Myfile.read()
print(content)
Myfile.close()

#Fruits # Creating a file and writing a list of fruits to it
Fruits = open("Fruits.txt", "w")
Fruitlist = ["Apple", "Banana", "Cherry", "Date", "Elderberry","Fig", "Grape", "Honeydew"]
for item in Fruitlist:
    Fruits.write(item + "\n")
Fruits.close()