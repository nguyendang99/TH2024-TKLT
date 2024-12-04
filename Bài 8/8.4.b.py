print("DANG NGUYEN DANG")
print("MSSV: 235752021610010")
print("#############################")
######################################
import tkinter as tk
#Hàm xử lý sự kiện khu button được nhấn
def button_clicked():
    print("Button clicked!")
#Tạo một cửa sổ đồ hoạ
window=tk.Tk()
#Thiết lập tiêu đề cửa sổ
window.title("Window Form")
#Thiết lập kích thước
window.geometry("400x300")
#tạo một button
button=tk.Button(window,text="Click me!",command=button_clicked)
#đặt button vào cửa sổ
button.pack()
#Hiện thị cửa sổ đồ hoạ
window.mainloop()
