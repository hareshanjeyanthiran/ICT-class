def one_iteration(a, b):
    return a * b

def n_iterations(a, b):
    result = 0
    for i in range(b):
        result = result + a
    return result

a = int(input("Enter 'a' for a*b: "))
b = int(input("Enter 'b' for a*b: "))

print("1 iteration:", one_iteration(a, b))
print("N iteration:", n_iterations(a, b))