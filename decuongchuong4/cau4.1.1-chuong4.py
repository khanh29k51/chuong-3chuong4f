n,k=map(int,input().split())
A = set(map(int,input().split()))
K = list(map(int,input().split()))
for i in K:
    if i in A:
        print("YES")
    else:
        print("NO")



