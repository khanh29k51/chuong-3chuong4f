def ucln(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def bcnn(a, b):
    return abs(a * b) // ucln(a, b)
a = int(input())
b = int(input())
print(bcnn(a,b))
