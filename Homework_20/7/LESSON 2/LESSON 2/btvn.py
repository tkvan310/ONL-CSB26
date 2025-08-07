def tinh_trung_binh_chan(lst):
    so_chan = [x for x in lst if x % 2 == 0]
    if len(so_chan) == 0:
        return None
    return sum(so_chan) / len(so_chan)


ds = [1, 2, 4, 7, 8, 9]
kq = tinh_trung_binh_chan(ds)
print("Trung bình các số chẵn:", kq)