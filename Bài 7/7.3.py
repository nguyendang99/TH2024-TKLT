print("DANG NGUYEN DANG")
print("MSSV: 235752021610010")
print("#############################")
######################################
filename = 'data.txt'  
try:
    with open(filename, 'r') as file:  
        content = file.read() 
        print(content)
except FileNotFoundError:
    print(f"File '{filename}' không tồn tại.")
except Exception as e:
    print(f"Đã xảy ra lỗi: {e}")
