print("DANG NGUYEN DANG")
print("MSSV: 235752021610010")
print("#############################")
######################################
import tkinter as tk
# Hàm xử lý sự kiện khi button được nhấn
def button_clicked():
    print("Button clicked!")
# Tạo một cửa sổ đồ họa
window = tk.Tk()
window.title("nd")
window.geometry("400x300")
# Tạo một button với màu nền và màu chữ tùy chỉnh
button = tk.Button(window, text="Click me!", command=button_clicked, bg="blue", fg="white")
# Đặt button vào cửa sổ
button.pack()
# Hiện thị cửa sổ đồ họa
window.mainloop()
