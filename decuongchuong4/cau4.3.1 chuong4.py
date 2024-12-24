def dem_so_k(bang_so, k):
    dem = 0
    for hang in bang_so:
        for phan_tu in hang:
            if phan_tu == k:
                dem += 1
    return dem

if __name__ == "__main__":
    m, n, k = map(int, input().split())
    bang_so = []
    for _ in range(m):
        hang = list(map(int, input().split()))
        bang_so.append(hang)
    ket_qua = dem_so_k(bang_so, k)
    print(ket_qua)