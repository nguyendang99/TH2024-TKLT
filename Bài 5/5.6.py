print("DANG NGUYEN DANG")
print("MSSV: 235752021610010")
print("#############################")
######################################
def sort_list(lst):
    return sorted(lst)
def find_max(lst):
    max_value = max(lst)
    max_index = lst.index(max_value)
    return max_value, max_index
def find_min(lst):
    min_value = min(lst)
    min_index = lst.index(min_value)
    return min_value, min_index
def main():
    n = int(input("Nhập số lượng phần tử trong danh sách: "))
    lst = []
    for i in range(n):
        value = int(input(f"Nhập phần tử thứ {i + 1}: "))
        lst.append(value)
    sorted_lst = sort_list(lst)
    print("Danh sách đã sắp xếp:", sorted_lst)
    max_value, max_index = find_max(lst)
    min_value, min_index = find_min(lst)
    print("Phần tử lớn nhất:", max_value, "ở vị trí", max_index)
    print("Phần tử nhỏ nhất:", min_value, "ở vị trí", min_index)
if __name__ == "__main__":
    main()
