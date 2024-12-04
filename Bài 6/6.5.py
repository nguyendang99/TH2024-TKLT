print("DANG NGUYEN DANG")
print("MSSV: 235752021610010")
print("#############################")
######################################
class StringReversal:
    def __init__(self, input_string):
        self.input_string = input_string
    def reverse_words(self):
        words = self.input_string.split()
        reversed_words = words[::-1]      
        return ' '.join(reversed_words)    
input_string = 'hello .py'
string_reversal = StringReversal(input_string)
print(string_reversal.reverse_words())
