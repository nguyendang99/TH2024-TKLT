print("DANG NGUYEN DANG")
print("MSSV: 235752021610010")
print("#############################")
######################################
from tkinter import *
def NewFile():
    print("New File!")
def OpenFile():
    print("Open File!")
def Exit():
    print("Exit File!")
    root.quit()
def InsertText():
    print("Insert Text")
def InsertPicture():
    print("Insert Picture")
def About():
    print("This is a simple example of a menu")
root = Tk()
root.title("nd")
#Tạo thanh menu chính
menubar = Menu(root)
root.config(menu=menubar)
#Tạo menu File
filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=NewFile)
filemenu.add_command(label="Open", command=OpenFile)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=Exit)
#Tạo menu Insert
insertmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Insert", menu=insertmenu)
insertmenu.add_command(label="Text", command=InsertText)
insertmenu.add_command(label="Picture", command=InsertPicture)
#Tạo menu help
helpmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=About)

root.mainloop()
