def tong_chu_so(n):
    n = abs(n)
    tong = 0
    while n > 0:
        tong += n % 10
        n //= 10
    return tong
n = int(input())
print(tong_chu_so(n))