print("DANG NGUYEN DANG")
print("MSSV: 235752021610010")
print("#############################")
######################################
input_file = open('C:/Users/ASUS/Documents/data.txt', 'r')
char, wc, lc = 0, 0, 0
for line in input_file:
    char += len(line)     
    words = line.split()
    wc += len(words)
    lc += 1 
input_file.close()
print("Số ký tự là %d\nSố từ là %d\nSố dòng là %d" % (char, wc, lc))
