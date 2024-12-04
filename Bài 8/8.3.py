print("DANG NGUYEN DANG")
print("MSSV: 235752021610010")
print("#############################")
######################################
import turtle
import random
#Tạo danh sách màu sắc
colors = ["red", "green", "pink", "orange", "purple", "blue", "yellow"]
#Tạo một cửa sổ vẽ và một con rùa(turtle)
window = turtle.Screen()
painter = turtle.Turtle()
painter.pensize(3)  # Đặt kích thước bút vẽ
#Vẽ 12 hình tròn với màu sắc ngẫu nhiên
for i in range(12):
    #Chọn màu ngẫu nhiên
    color = random.choice(colors)
    painter.pencolor(color)
    #Vẽ hình tròn
    painter.circle(100)
    #Xoay và di chuyển rùa
    painter.right(30)
    painter.left(60)
    painter.setposition(0, 0)
turtle.done()
