s= input()
danhsachdem = {}
for char in s:
    if char in danhsachdem:
        danhsachdem[char] += 1
    else:
        danhsachdem[char] = 1
for char, so_lan in danhsachdem.items():
    print(f"'{char}': {so_lan}")

ss