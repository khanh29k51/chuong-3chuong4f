def thap_phan_sang_thap_luc_phan(n):
    if n == 0:
        return "0"
    
    he_thap_luc_phan = "0123456789ABCDEF"
    x = ""
    
    while n > 0:
        du = n % 16
        x= he_thap_luc_phan[du] + x
        n = n // 16
    
    return x

n = int(input())
print(thap_phan_sang_thap_luc_phan(n))
