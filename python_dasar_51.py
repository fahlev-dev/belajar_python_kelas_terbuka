'''belajar kwargs'''

def fungsi(nama, tinggi, berat):
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")

fungsi("ucup", 170, 60)

def fungsi(**data):
    nama = data["nama"]
    tinggi = data["tinggi"]
    berat = data["berat"]
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")

fungsi(nama = "ucup", tinggi = 180, berat = 60)

def math(*args, **kwargs):
    output = 0
    if kwargs["option"] == "tambah":
        for angka in args:
            output += angka
    elif kwargs["option"] == "kali":
        output = 1
        for angka in args:
            output *= angka
    elif kwargs["option"] == "bagi":
        output = 1
        for angka in args:
            output /= angka
    elif kwargs["option"] == "kurang":
        for angka in args:
            output -= angka
    else:
        print("tidak ada pilihan")
    
    return output

hasil = math(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, option = "tambah")
print(hasil)
hasil = math(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, option = "kali")
print(hasil)