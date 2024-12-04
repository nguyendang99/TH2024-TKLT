print("DANG NGUYEN DANG")
print("MSSV: 235752021610010")
print("#############################")
######################################
def benefit(t, n, k):
    A = n * (1 + t / 100) ** k
    return A
try:
    t = float(input("Nhập lãi suất tháng (t%): "))
    n = float(input("Nhập số vốn ban đầu (n): "))
    k = int(input("Nhập số tháng gửi (k): "))
    result = benefit(t, n, k)
    print(f"Số tiền nhận được sau {k} tháng là: {result:.2f}")

except ValueError:
    print("Lỗi! Vui lòng nhập giá trị hợp lệ.")
