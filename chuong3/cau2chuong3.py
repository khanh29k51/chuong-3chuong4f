import math

def so_nguyen_to(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    else:
        for i in range(5, int(math.sqrt(n)) + 1, 1):
            if n % i == 0 or n % (i + 2) == 0:
                return False
        return True

n = int(input())
for i in range (1,n):
   if so_nguyen_to(i):
      print(i,end="")
