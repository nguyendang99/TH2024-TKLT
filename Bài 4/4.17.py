print("DANG NGUYEN DANG")
print("MSSV: 235752021610010")
print("#############################")
######################################
def sum_of_divisors(num):
    total = 0
    for i in range(1, num):
        if num % i == 0:
            total += i
    return total
n = int(input("Nhập số n: "))
print("Các số thỏa mãn là:")
for i in range(1, n):
    if sum_of_divisors(i) > i:
        print(i)
