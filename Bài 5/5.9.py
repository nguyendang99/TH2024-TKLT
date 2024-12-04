print("DANG NGUYEN DANG")
print("MSSV: 235752021610010")
print("#############################")
######################################
def binary_search(sorted_list, value):
    lower_bound = 0
    upper_bound = len(sorted_list) - 1

    while lower_bound <= upper_bound:
        mid_point = lower_bound + (upper_bound - lower_bound) // 2
        if sorted_list[mid_point] < value:
            lower_bound = mid_point + 1
        elif sorted_list[mid_point] > value:
            upper_bound = mid_point - 1
        else:
            return True  
    return False  
def main():
    n = int(input("Nhập số lượng phần tử trong danh sách: "))
    lst = []
    for i in range(n):
        value = int(input(f"Nhập phần tử thứ {i + 1}: "))
        lst.append(value)
    sorted_list = sorted(lst)
    print("Danh sách đã sắp xếp:", sorted_list)
    search_value = int(input("Nhập phần tử cần tìm: "))
    if binary_search(sorted_list, search_value):
        print(f"Phần tử {search_value} có trong danh sách.")
    else:
        print(f"Phần tử {search_value} không có trong danh sách.")
if __name__ == "__main__":
    main()
