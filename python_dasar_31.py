data_angka = [1,3,4,6,3,6,7,9,6,1,3,5,6,7,8,9,5,42,3,1,2,3,4]

print(f"data angka : \n{data_angka}")

print(f"jumlah data angka 3 : {data_angka.count(3)}")

data = ["Ucup", "Otong", "Dudung", "Ujang"]
print(f"data = {data}")

index_dudung = data.index("Dudung")
index_ujang = data.index("Ujang")
print(f"index dudung = {index_dudung}")
print(f"index ujang = {index_ujang}")

# urutkan list
print(f"data angka sebelum di sort : {data_angka}")
data_angka.sort()
print(f"data angka setelah di sort : {data_angka}")

print(f"data : {data}")
data.sort()
print(f"data sort : {data}")

data_angka.reverse()
data.reverse()

print(f"data angka reverse : {data_angka}")
print(f"data reverser : {data}")