'''belajar anonymous function'''

def f_kuadrat(angka):
    return angka ** 2

print(f"hasil fungsi kuadrat = {f_kuadrat(3)}")

kuadrat = lambda angka: angka ** 2
print(f"hasil lambda kuadrat = {kuadrat(8)}")

pangkat = lambda num, pow : num ** pow
print(f"hasil lambda pangkat = {pangkat(5, 2)}")

data_list = ["Otong", "Ucup", "Dudung"]
data_list.sort()
print(f"sorted list = {data_list}")

data_list.sort(key = len)
print(f"sorted list = {data_list}")

def panjang_nama(nama):
    return len(nama)

data_list.sort(key = panjang_nama)
print(f"sorted list by panjang = {data_list}")

data_list = ["Otong", "Ucup", "Dudung"]
data_list.sort(key = lambda nama: len(nama))
print(f"sorted list by lambda = {data_list}")

data_angka = [1,2,3,4,5,6,7,8,9,10,11,12]

def kurang_dari_lima(angka):
    return angka < 5

# data < 5
data_angka_baru = list(filter(kurang_dari_lima, data_angka))
data_angka_baru = list(filter(lambda x : x < 7, data_angka))
print(data_angka_baru)

# data genap
data_genap = list(filter(lambda x : (x % 2 == 0), data_angka))
print(data_genap)

# data ganjil
data_ganjil = list(filter(lambda x : (x % 2 == 1), data_angka))
print(data_ganjil)

def pangkat(n):
    return lambda angka : angka ** n

pangkat2 = pangkat(2)
print(f"pangkat 2 = {pangkat2(5)}")