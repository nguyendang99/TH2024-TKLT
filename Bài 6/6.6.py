print("DANG NGUYEN DANG")
print("MSSV: 235752021610010")
print("#############################")
######################################
class StringProcessor:
    def __init__(self):
        self.input_string = ""
    def get_String(self):
        self.input_string = input("Nhập một chuỗi: ")
    def print_String(self):
        print(self.input_string.upper())
processor = StringProcessor()
processor.get_String()
processor.print_String()
