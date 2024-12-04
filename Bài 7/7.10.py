print("DANG NGUYEN DANG")
print("MSSV: 235752021610010")
print("#############################")
######################################
filename = 'text.txt'  
try:
    with open(filename, 'r') as file:
        text = file.read()  
    import string
    text = text.lower()  
    text = text.translate(str.maketrans('', '', string.punctuation))  
    words = text.split()  
    max_length = max(len(word) for word in words)
    longest_words = [word for word in words if len(word) == max_length]
    print(f"Những từ dài nhất có độ dài {max_length}:")
    for word in longest_words:
        print(word)
except FileNotFoundError:
    print(f"Không tìm thấy tệp '{filename}'.")
except Exception as e:
    print(f"Đã xảy ra lỗi: {e}")
