print("DANG NGUYEN DANG")
print("MSSV: 235752021610010")
print("#############################")
######################################
input_string = input("Nhập các số (phân tách bởi dấu phẩy): ")
numbers = [int(num) for num in input_string.split(',')]
odd_numbers = [num for num in numbers if num % 2 != 0]
print(",".join(map(str, odd_numbers)))
