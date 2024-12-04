print("DANG NGUYEN DANG")
print("MSSV: 235752021610010")
print("#############################")
######################################
import tkinter as tk
def submit_form():
    # Lấy thông tin từ các trường nhập liệu
    ho_ten = entry_ho_ten.get()
    ngay_sinh = entry_ngay_sinh.get()
    mssv =entry_mssv.get()
    nganh_hoc =entry_nganh_hoc.get()
    #In thông tin cá nhân
    print("Họ và tên:",ho_ten)
    print("Ngày sinh:",ngay_sinh)
    print("MSSV:",mssv)
    print("Ngành học:",nganh_hoc)
# Tạo cửa sổ chính
window = tk.Tk()
window.title("Form đăng ký thông tin cá nhân")
# Tạo và định dạng các thành phần trong form
label_ho_ten= tk.Label(window, text="Họ và tên:")
entry_ho_ten= tk.Entry(window)
label_ngay_sinh= tk.Label(window, text="Ngày sinh:")
entry_ngay_sinh= tk.Entry(window)
label_mssv= tk.Label(window, text="MSSV:")
entry_mssv= tk.Entry(window)
label_nganh_hoc= tk.Label(window, text="Ngành học:")
entry_nganh_hoc= tk.Entry(window)
# Tạo nút button
button_submit = tk.Button(window, text="Gửi", command=submit_form)
#định vị các thành phần trong from
label_ho_ten.grid(row=0, column=0,sticky=tk.E)
entry_ho_ten.grid(row=0, column=1)
label_ngay_sinh.grid(row=1, column=0,sticky=tk.E)
entry_ngay_sinh.grid(row=1, column=1)
label_mssv.grid(row=2, column=0,sticky=tk.E)
entry_mssv.grid(row=2, column=1)
label_nganh_hoc.grid(row=3, column=0,sticky=tk.E)
entry_nganh_hoc.grid(row=3, column=1)
button_submit.grid(row=4,columnspan=2)
#chạy vòng lặp chính của giao diện
window.mainloop()
