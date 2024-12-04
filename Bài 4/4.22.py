print("DANG NGUYEN DANG")
print("MSSV: 235752021610010")
print("#############################")
######################################
even_digit_numbers = []
for number in range(1000, 3001):
    if all(int(digit) % 2 == 0 for digit in str(number)):
        even_digit_numbers.append(str(number))
print(",".join(even_digit_numbers))
