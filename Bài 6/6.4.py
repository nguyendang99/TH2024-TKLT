print("DANG NGUYEN DANG")
print("MSSV: 235752021610010")
print("#############################")
######################################
class RomanToInt:
    def __init__(self):
        self.roman_map = {'I': 1,'V': 5,'X': 10,'L': 50,'C': 100,'D': 500,'M': 1000}
    def convert(self, roman):
        total = 0
        prev_value = 0
        for char in reversed(roman):
            value = self.roman_map[char]
            if value < prev_value:
                total -= value
            else:
                total += value
            prev_value = value
        return total
roman_converter = RomanToInt()
roman_number = "IX"
print(f"Số La Mã {roman_number} chuyển thành số nguyên là: {roman_converter.convert(roman_number)}")
roman_number = "XLII"
print(f"Số La Mã {roman_number} chuyển thành số nguyên là: {roman_converter.convert(roman_number)}")
roman_number = "MCMXCIV"
print(f"Số La Mã {roman_number} chuyển thành số nguyên là: {roman_converter.convert(roman_number)}")
