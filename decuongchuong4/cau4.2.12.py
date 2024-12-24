s = input()
tong = 0
sotamthoi = "" 
for char in s:
    if char.isdigit():  
       sotamthoi += char
    else:
        if sotamthoi: 
            tong += int(sotamthoi)
            sotamthoi = ""  
if sotamthoi:
    tong += int(sotamthoi)
print(tong)
