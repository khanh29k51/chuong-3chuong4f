def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

n = int(input())
so_fibonacci = [fibonacci(i) for i in range(1, n + 1)]
for i in so_fibonacci:
   print(i,end=" ")
print({sum(so_fibonacci)})
