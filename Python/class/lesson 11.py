class customer:
    def __init__(self, id, name, email, age):
        self.__id = id
        self.name = name
        self.__email = email
        self.age = age

    def getDetails(self):
        print("Customer ID: ", self.__id)
        print("Customer Name: ", self.name)
        print("Customer Email: ", self.__email)
        print("Customer Age: ", self.age)

Jileshan = customer(1, "Jileshan", "jileshan@example.com", 10)
Hareshan = customer(2, "Hareshan", "hareshan@example.com", 13)
Sam = customer(3, "Sam", "sam@example.com", 22)
Kartik = customer(4, "Kartik", "kartik@example.com", 14)

class Bank:
    def __init__(self, id, balance):
        self.id = id
        self.__balance = balance

    def setBalance(self, new_balance):
        self.__balance = new_balance

    def getBalance(self):
        print("Current balance is: ", self.__balance)

Jileshan = Bank(1, 1000)
Hareshan = Bank(2, 2000)
Sam = Bank(3, 3000)
Kartik = Bank(4, 4000)



print("Hareshan's account details:")
print("ID: ", Hareshan.id)
print("Hareshan's initial balance is: ")
Hareshan.getBalance()
Hareshan.setBalance(5000)
print("Hareshan's new balance is: ")
Hareshan.getBalance()

print("Jileshan's account details:")
print("ID: ", Jileshan.id)
print("Jileshan's initial balance is: ")
Jileshan.getBalance()
Jileshan.setBalance(1500)
print("Jileshan's new balance is: ")
Jileshan.getBalance()

print("Sam's account details:")
print("ID: ", Sam.id)
print("Sam's initial balance is: ")
Sam.getBalance()
Sam.setBalance(3500)
print("Sam's new balance is: ")
Sam.getBalance()

print("Kartik's account details:")
print("ID: ", Kartik.id)
print("Kartik's initial balance is: ")
Kartik.getBalance()
Kartik.setBalance(4500)
print("Kartik's new balance is: ")
Kartik.getBalance()