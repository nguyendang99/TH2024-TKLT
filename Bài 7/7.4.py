print("DANG NGUYEN DANG")
print("MSSV: 235752021610010")
print("#############################")
######################################
def file_read_from_head(fname, nlines):
    from itertools import islice
    with open(fname) as f:
        for line in islice(f, nlines):
            print(line)

file_read_from_head('test.txt', 2)
