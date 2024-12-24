S = input()
N  =[]
for char in S:
    if char.isdigit():
        N.append(char)
print(max(N))