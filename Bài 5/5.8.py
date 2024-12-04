print("DANG NGUYEN DANG")
print("MSSV: 235752021610010")
print("#############################")
######################################
def Sequential_Search(dlist, item):
    for index, value in enumerate(dlist):
        if value == item:
            return True, index  
    return False, -1
def main():
    n = int(input("Nhập số lượng phần tử trong danh sách: "))
    dlist = []
    for i in range(n):
        value = int(input(f"Nhập phần tử thứ {i + 1}: "))
        dlist.append(value)
    item = int(input("Nhập phần tử cần tìm: "))
    found, position = Sequential_Search(dlist, item)
    if found:
        print(f"Phần tử {item} được tìm thấy ở vị trí {position}.")
    else:
        print(f"Phần tử {item} không có trong danh sách.")
if __name__ == "__main__":
    main()
