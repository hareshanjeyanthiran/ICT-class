def binary_to_decimal(binary_str):
    decimal = 0
    length = len(binary_str)

    for i in range(length):
        digit = binary_str[i]
        if digit == '1':
            power = length - 1 - i
            decimal += 2 ** power
        elif digit != '0':
            return "Invalid binary number!"

    return decimal


binary_input = input("Enter a binary number: ")
result = binary_to_decimal(binary_input)

print("Decimal value:", result)