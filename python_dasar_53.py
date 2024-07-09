'''global dan local scope'''

nama_global = "otong" # variabel global bisa di akses di dalam fungsi

def fungsi():
    print(f"fungsi menampilkan {nama_global}")

fungsi()

for i in range(0,5):
    print(f"loop {i} - {nama_global}")

if True:
    print(f"if menampilkan {nama_global}")

def fungsi2():
    nama_local = "ucup" # variabel local scope hanya bisa di akses di dalam fungsi itu sendiri

fungsi2()

angka = 0
nama = "ucup"

def ubah(nilai_baru, nama_baru):
    global angka
    global nama
    angka = nilai_baru
    nama = nama_baru

print(f"sebelum {angka, nama}")
ubah(10, "otong")
print(f"sesudah {angka, nama}")