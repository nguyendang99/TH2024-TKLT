print("DANG NGUYEN DANG")
print("MSSV: 235752021610010")
print("#############################")
######################################
source_filename = 'source.txt'
destination_filename = 'destination.txt'  

try:
    with open(source_filename, 'r') as source_file:
        content = source_file.read()
    with open(destination_filename, 'w') as destination_file:
        destination_file.write(content)
    
    print(f"Đã sao chép nội dung từ '{source_filename}' sang '{destination_filename}' thành công.")
    
except FileNotFoundError:
    print(f"Không tìm thấy tệp '{source_filename}'.")
except Exception as e:
    print(f"Đã xảy ra lỗi: {e}")
