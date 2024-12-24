def so_hoan_hao(n):
    if n <= 1:
        return False
    
    tong = 0
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            tong += i
    return tong == n
a = int(input())
b=int(input())
for i in range (a+1,b):
    if so_hoan_hao(i):
        print(i,end="")