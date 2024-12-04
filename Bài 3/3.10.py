print("DANG NGUYEN DANG")
print("MSSV: 235752021610010")
print("#############################")
######################################
# Hàm cộng hai số
def add(x, y):
    return x + y

# Hàm trừ hai số
def subtract(x, y):
    return x - y

# Hàm nhân hai số
def multiply(x, y):
    return x * y

# Hàm chia hai số
def divide(x, y):
    # Kiểm tra chia cho 0
    if y == 0:
        return "Lỗi! Không thể chia cho 0."
    return x / y

# Hiển thị menu cho người dùng chọn phép toán
print("Chọn phép toán:")
print("1. Cộng")
print("2. Trừ")
print("3. Nhân")
print("4. Chia")

# Yêu cầu người dùng nhập lựa chọn phép toán
choice = input("Nhập lựa chọn (1/2/3/4): ")

# Kiểm tra nếu lựa chọn là hợp lệ
if choice not in ['1', '2', '3', '4']:
    print("Lựa chọn không hợp lệ! Vui lòng chọn một phép toán hợp lệ.")
else:
    # Yêu cầu người dùng nhập hai số
    try:
        num1 = float(input("Nhập số thứ nhất: "))
        num2 = float(input("Nhập số thứ hai: "))
    except ValueError:
        print("Lỗi! Vui lòng nhập vào một số hợp lệ.")
        exit()

    # Thực hiện phép toán dựa trên lựa chọn của người dùng
    if choice == '1':
        print(f"{num1} + {num2} = {add(num1, num2)}")
    elif choice == '2':
        print(f"{num1} - {num2} = {subtract(num1, num2)}")
    elif choice == '3':
        print(f"{num1} * {num2} = {multiply(num1, num2)}")
    elif choice == '4':
        result = divide(num1, num2)
        if isinstance(result, float):
            print(f"{num1} / {num2} = {result}")
        else:
            print(result)  # In thông báo lỗi chia cho 0
