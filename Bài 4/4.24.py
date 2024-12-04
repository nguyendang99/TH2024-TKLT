print("DANG NGUYEN DANG")
print("MSSV: 235752021610010")
print("#############################")
######################################
input_string = input("Nhập một câu: ")
uppercase_count = 0
lowercase_count = 0
for char in input_string:
    if char.isupper():  
        uppercase_count += 1
    elif char.islower():  
        lowercase_count += 1
print("Chữ hoa:", uppercase_count)
print("Chữ thường:", lowercase_count)
