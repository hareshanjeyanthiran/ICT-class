# list
fruits = ["Apple","Grape","Blueberry","Watermelon","Banana"]
# Operation on list
newfruits = ["Mango","Avagado","Kiwi","Papaya"]
#accessing element
print(fruits[0])
print(fruits[3])

#slicing
print(fruits[1:4])

# Add an element
fruits.append("Peach")
fruits.append("Guava")

#Add in perticular position
fruits.insert(2,"Strawberry")

# Add a new list
fruits.extend(newfruits)


#how to remove elemnt
fruits.remove("Apple")
fruits.remove("Papaya")


#remove using index
fruits.pop(1)


fruits.sort()
fruits.reverse()
#Clearing
# fruits.clear()

print(fruits)