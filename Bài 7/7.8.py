print("DANG NGUYEN DANG")
print("MSSV: 235752021610010")
print("#############################")
######################################
my_list = ["Hello, world!", "This is a test file.", "Python is awesome!"]
filename = 'output.txt'
try:
    with open(filename, 'w') as file: 
        for item in my_list:
            file.write(item + '\n') 
    print(f"Nội dung danh sách đã được ghi vào tệp '{filename}' thành công.")
except Exception as e:
    print(f"Đã xảy ra lỗi: {e}")
