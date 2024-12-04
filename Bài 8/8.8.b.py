print("DANG NGUYEN DANG")
print("MSSV: 235752021610010")
print("#############################")
######################################
import tkinter as tk
def show_result():
    #Lấy giá trị của nút radio được chọn
    selected_value=selected.get()
    #Hiển thị kết quả
    result_label.config(text=f"Bạn đã chọn: {selected_value}")
#Tạo cửa sổ chính
window= tk.Tk()
window.title("Welcome")
#Tạo các biến để lưu giá trị của các nút radio
selected =tk.StringVar()
#Tạo các nút radio
radio1=tk.Radiobutton(window,text="First",variable=selected,value=1)
radio2=tk.Radiobutton(window,text="Second",variable=selected,value=2)
radio3=tk.Radiobutton(window,text="Third",variable=selected,value=3)
#Tạo nút nhấn
button=tk.Button(window,text="Click Me",command=show_result)
#Tạo label để hiển thị kết quả
result_label=tk.Label(window)
#Đặt các phần tử lên cửa sổ
radio1.pack()
radio2.pack()
radio3.pack()
button.pack()
result_label.pack()
#Chạy vòng lặp sự kiện
window.mainloop()
