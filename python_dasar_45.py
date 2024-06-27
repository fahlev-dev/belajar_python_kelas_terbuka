# fungsi dengan argumen

# def hello_world(nama = "template"):
#     print(f"Selamat datang dunia wahai {nama}")

# hello_world("Kosasih")

# def tambah(angka1, angka2):
#     hasil = angka1 + angka2
#     print(f"{angka1} + {angka2} = {hasil}")

# tambah(10, 10)

def say_hi(list_peserta):
    '''fungsi say hi'''
    data_peserta = list_peserta.copy()
    for peserta in data_peserta:
        print(f"yang terhormat {peserta}")

anggota_boyband = ["ucup", "otong", "dudung"]

say_hi(anggota_boyband)