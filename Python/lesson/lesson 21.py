word = str(input("Enter the word: "))
reverse = ""


for l in word.lower():
    reverse = l+reverse

if word.lower()==reverse:
    print("Palindrome")
else:
    print("Not palindrome")