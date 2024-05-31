# manipulasi list

data = ["ucup", "otong", "janda"]
print(f"data index pertama: {data[0]}")

print(f"data index terakhir: {data[-1]}")

print(f"panjang data = {len(data)}")

print(f"data sebelum di tambah : {data}")

data.insert(1, "Asep")

print(f"data setelah di tambah : {data}")

data.append("Jajang")

print(f"data setelah di tambah : {data}")

data_baru = ["Ujang", "Usep", "Dadang"]

data.extend(data_baru)
print(f"data setelah di gabungkan : {data}")

data[2] = "Michael"
print(f"data index ke 2 yang di ubah : {data}")

data.remove("Ujang")
print(f"data yang di hapus : {data}")

data.pop()
print(f"data terkahir yang di hapus : {data}")