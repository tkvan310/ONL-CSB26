# Bài 8: Hàm kiểm tra số chẵn
# Viết hàm loc_chan(ds) nhận danh sách số và trả về danh sách các số chẵn.

def loc_chan(ds):
    return [so for so in ds if so % 2 == 0]

danh_sach = [1,2,3,4,5,6,7,8,9,10]
loc_so_chan = loc_chan(danh_sach)
print("Danh sách các số chẵn là :",loc_so_chan)

        

