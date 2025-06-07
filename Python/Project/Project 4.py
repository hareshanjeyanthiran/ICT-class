# Input from user
num = int(input("Enter a number: "))

original_num = num

order = 0
temp = num
while temp > 0:
    temp //= 10
    order += 1


temp = num
armstrong_sum = 0

while temp > 0:
    digit = temp % 10
    armstrong_sum += digit ** order
    temp //= 10

if armstrong_sum == original_num:
    print(f"{original_num} is an Armstrong number.")
else:
    print(f"{original_num} is not an Armstrong number.")

