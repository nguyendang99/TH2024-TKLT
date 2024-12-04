print("DANG NGUYEN DANG")
print("MSSV: 235752021610010")
print("#############################")
######################################
def bubbleSort(nlist):
    n = len(nlist)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if nlist[j] > nlist[j + 1]:
                nlist[j], nlist[j + 1] = nlist[j + 1], nlist[j]
                swapped = True
        if not swapped:
            break
    return nlist
def main():
    n = int(input("Nhập số lượng phần tử trong danh sách: "))
    nlist = []
    for i in range(n):
        value = int(input(f"Nhập phần tử thứ {i + 1}: "))
        nlist.append(value)
    sorted_list = bubbleSort(nlist)
    print("Danh sách sau khi sắp xếp:", sorted_list)
if __name__ == "__main__":
    main()
