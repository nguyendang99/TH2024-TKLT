print("DANG NGUYEN DANG")
print("MSSV: 235752021610010")
print("#############################")
######################################
import turtle

# Thiết lập màn hình
window = turtle.Screen()
window.bgcolor('lightgreen')

# Tạo con turtle để vẽ
painter = turtle.Turtle()
painter.fillcolor('blue')
painter.pencolor('blue')
painter.pensize(3)

# Hàm vẽ hình vuông
def drawsq(t, s):
    for i in range(4):
        t.forward(s)
        t.left(90)

# Vẽ các hình vuông xung quanh một vòng tròn
for i in range(18):  # 18 lần để vẽ 18 hình vuông xung quanh vòng tròn
    drawsq(painter, 200)
    painter.left(20)  # Quay một góc để tạo hiệu ứng xoay tròn

# Đóng cửa sổ khi click chuột
window.exitonclick()
