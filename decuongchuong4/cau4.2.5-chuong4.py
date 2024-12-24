s = input().strip()
chuhoa = 0
chuthuong = 0
chuso = 0
for char in s:
    if char.isupper():
       chuhoa += 1
    elif char.islower():
       chuthuong += 1
    elif char.isdigit():
        chuso += 1

print(chuhoa,chuthuong,chuso)
