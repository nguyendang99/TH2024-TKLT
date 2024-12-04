
print("DANG NGUYEN DANG")
print("MSSV: 235752021610010")
print("#############################")
######################################
# Mở file để đọc
input_file = open('data.txt', 'r')

# Đọc từng dòng trong file và đảo ngược từng dòng
for line in input_file:
    line = line.strip()  # Loại bỏ ký tự trắng ở đầu và cuối dòng
    s = ''
    for i in range(len(line) - 1, -1, -1):  # Lặp qua dòng từ cuối đến đầu
        s += line[i]
    print(s)

# Đóng file sau khi hoàn thành
input_file.close()

