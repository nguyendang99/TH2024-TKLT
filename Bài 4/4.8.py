print("DANG NGUYEN DANG")
print("MSSV: 235752021610010")
print("#############################")
######################################
day_tu = input("Nhập dãy các từ: ").split()
do_dai_lon_nhat = max(len(tu) for tu in day_tu)
tu_dai_nhat = [tu for tu in day_tu if len(tu) == do_dai_lon_nhat]
print("Các từ dài nhất:", " ".join(tu_dai_nhat))
