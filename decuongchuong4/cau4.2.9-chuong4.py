chuoi = input().strip()
danh_sach_so = chuoi.split(',')
for so in danh_sach_so:
    if int(so) % 2 != 0:
        print(so)
