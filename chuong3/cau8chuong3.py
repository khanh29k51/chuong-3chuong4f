def thapphan_nhiphan(n):
    if n == 0:
        return "0"
    nhi_phan = ""
    while n > 0:
        nhi_phan = str(n % 2) + nhi_phan
        n //= 2
    return nhi_phan
n = int(input())
print(thapphan_nhiphan(n))
