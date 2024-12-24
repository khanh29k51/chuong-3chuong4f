def giai_thua(n):
    if n < 0:
        return "loi"
    x = 1
    for i in range(2, n + 1):
       x *= i
    return x

n = input()
try:
    n = int(n)
    print(giai_thua(n))
except ValueError:
    print("loi")
