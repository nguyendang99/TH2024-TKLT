print("DANG NGUYEN DANG")
print("MSSV: 235752021610010")
print("#############################")
######################################
import tkinter as tk
root = tk.Tk()
v = tk.IntVar()
v.set(1)  # Khởi tạo lựa chọn, tức là Python
languages = [
    ("Python",1),
    ("Perl",2),
    ("Java",3),
    ("C++",4),
    ("C",5)
]
def ShowChoice():
    print(v.get())
tk.Label(root,
        text="""Chọn ngôn ngữ lập trình yêu thích của bạn:""",
        justify=tk.LEFT,
        padx=20).pack()
for val, language in enumerate(languages):
    tk.Radiobutton(root,
                  text=language,  # Chỉ hiển thị tên ngôn ngữ
                  indicatoron=0,  # Ẩn nút tròn
                  width=20,
                  padx=20,
                  variable=v,
                  command=ShowChoice,
                  value=val).pack(anchor=tk.W)
root.mainloop()



