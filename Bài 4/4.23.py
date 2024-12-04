print("DANG NGUYEN DANG")
print("MSSV: 235752021610010")
print("#############################")
######################################
input_string = input("Nhập một câu: ")
letter_count = 0
digit_count = 0
for char in input_string:
    if char.isalpha():  
        letter_count += 1
    elif char.isdigit():  
        digit_count += 1
print("Số chữ cái là:", letter_count)
print("Số chữ số là:", digit_count)
