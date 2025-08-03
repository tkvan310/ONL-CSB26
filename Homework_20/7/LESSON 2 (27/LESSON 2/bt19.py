# Bài 19: Sinh số ngẫu nhiên và ghi file
# Sinh 20 số ngẫu nhiên từ 1 đến 100, lưu vào file random.txt.

import random

so_ngau_nhien = [str(random.randint(1, 100)) for _ in range(20)]

with open("random.txt", "w") as f:
    f.write(" ".join(so_ngau_nhien))

print("Đã ghi 20 số ngẫu nhiên vào file random.txt")

