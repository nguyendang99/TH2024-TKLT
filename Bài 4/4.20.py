print("DANG NGUYEN DANG")
print("MSSV: 235752021610010")
print("#############################")
######################################
def combination(n, k):
    if k == 0 or k == n:
        return 1
    return combination(n - 1, k - 1) + combination(n - 1, k)
def print_pascals_triangle(n):
    for i in range(n):
        row = [combination(i, k) for k in range(i + 1)]
        print(" " * (n - i), " ".join(map(str, row)))
n = int(input("Nhập số n: "))
print_pascals_triangle(n)
