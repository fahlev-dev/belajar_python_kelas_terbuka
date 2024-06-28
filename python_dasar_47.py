'''default argument'''

def say_hello(nama = "ganteng"):
    print(f"hello {nama}")

say_hello("otong")
say_hello()

def sapa_dia(nama, pesan = "Apa Kabar"):
    '''fungsi dengan satu input biasa dan default argument'''
    print(f"hai {nama}, {pesan}")

sapa_dia("Dudung", "Hai Ganteng")
sapa_dia("Otong")

def hitung_pangkat(angka, pangkat):
    hasil = angka ** pangkat
    return hasil

print(hitung_pangkat(2, 4))

hasil = hitung_pangkat(angka = 5, pangkat = 2)
print(hasil)