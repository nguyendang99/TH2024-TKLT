print("DANG NGUYEN DANG")
print("MSSV: 235752021610010")
print("#############################")
######################################
import numpy as np
ids = np.array([101, 102, 103, 104, 105]) 
heights = np.array([1.70, 1.60, 1.80, 1.75, 1.65]) 
sorted_indices = np.lexsort((ids, heights))
print("Chỉ số sắp xếp:")
print(sorted_indices)
sorted_ids = ids[sorted_indices]
sorted_heights = heights[sorted_indices]

print("\nDữ liệu đã sắp xếp:")
for i in range(len(sorted_ids)):
    print(f"ID: {sorted_ids[i]}, Chiều cao: {sorted_heights[i]}")
