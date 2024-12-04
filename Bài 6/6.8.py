print("DANG NGUYEN DANG")
print("MSSV: 235752021610010")
print("#############################")
######################################
class ATM:
    def __init__(self):
        self.so_du = 10000  
        self.is_logged_in = False  
        self.username = "user" 
        self.password = "1234" 
    def login(self):
        print("Chào mừng bạn đến với ATM!")
        username_input = input("Nhập tên đăng nhập: ")
        password_input = input("Nhập mật khẩu: ")
        if username_input == self.username and password_input == self.password:
            self.is_logged_in = True
            print("Đăng nhập thành công!")
        else:
            print("Tên đăng nhập hoặc mật khẩu không đúng. Vui lòng thử lại.")
    def check_balance(self):
        if self.is_logged_in:
            print(f"Số dư tài khoản của bạn là: {self.so_du} VND")
        else:
            print("Bạn cần đăng nhập trước.")
    def withdraw(self):
        if self.is_logged_in:
            try:
                amount = float(input("Nhập số tiền bạn muốn rút: "))
                if amount > self.so_du:
                    print("Số dư không đủ để thực hiện giao dịch.")
                elif amount <= 0:
                    print("Số tiền rút phải lớn hơn 0.")
                else:
                    self.so_du -= amount
                    print(f"Bạn đã rút {amount} VND. Số dư còn lại: {self.so_du} VND")
            except ValueError:
                print("Vui lòng nhập một số hợp lệ.")
        else:
            print("Bạn cần đăng nhập trước.")

    def deposit(self):
        # Gửi tiền
        if self.is_logged_in:
            try:
                amount = float(input("Nhập số tiền bạn muốn gửi: "))
                if amount <= 0:
                    print("Số tiền gửi phải lớn hơn 0.")
                else:
                    self.so_du += amount
                    print(f"Bạn đã gửi {amount} VND. Số dư hiện tại: {self.so_du} VND")
            except ValueError:
                print("Vui lòng nhập một số hợp lệ.")
        else:
            print("Bạn cần đăng nhập trước.")
    def logout(self):
        self.is_logged_in = False
        print("Đã đăng xuất thành công. Hẹn gặp lại!")
def main():
    atm = ATM()
    while True:
        print("\n----- ATM -----")
        print("1. Đăng nhập")
        print("2. Kiểm tra số dư")
        print("3. Rút tiền")
        print("4. Gửi tiền")
        print("5. Đăng xuất")
        print("6. Thoát")
        try:
            choice = int(input("Chọn chức năng (1-6): "))
            if choice == 1:
                atm.login()
            elif choice == 2:
                atm.check_balance()
            elif choice == 3:
                atm.withdraw()
            elif choice == 4:
                atm.deposit()
            elif choice == 5:
                atm.logout()
            elif choice == 6:
                print("Thoát khỏi chương trình.")
                break
            else:
                print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")
        except ValueError:
            print("Vui lòng nhập một lựa chọn hợp lệ.")

if __name__ == "__main__":
    main()
