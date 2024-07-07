'''belajar args'''

def fungsi(nama, tinggi, berat):
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")

fungsi("ucup", 180, 80)

def fungsi(data_list):
    data = data_list.copy()
    nama = data[0]
    tinggi = data[1]
    berat = data[2]
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")

fungsi(["ucup", 100, 120])

def fungsi(*args):
    nama = args[0]
    tinggi = args[1]
    berat = args[2]
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")

fungsi("dudung", 120, 120)

def tambah(*data):
    output = 0
    for angka in data:
        output += angka

    return output

hasil = tambah(1, 2, 3, 4, 5)
print(f"hasilnya adalah = {hasil}")