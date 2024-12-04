print("DANG NGUYEN DANG")
print("MSSV: 235752021610010")
print("#############################")
######################################
import math
class Circle:
    def __init__(self, ban_kinh):
        self.ban_kinh = ban_kinh
    def tinh_dien_tich(self):
        return math.pi * (self.ban_kinh ** 2)
    def tinh_chu_vi(self):
        return 2 * math.pi * self.ban_kinh
circle = Circle(5)  
print(f"Diện tích hình tròn có bán kính {circle.ban_kinh} là: {circle.tinh_dien_tich():.2f}")
print(f"Chu vi hình tròn có bán kính {circle.ban_kinh} là: {circle.tinh_chu_vi():.2f}")
