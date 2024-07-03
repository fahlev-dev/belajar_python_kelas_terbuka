# latihan fungsi

import os

os.system('cls')

# print(f"{'PROGRAM MENGHITUNG LUAS':^40}")
# print(f"{'DAN KELILING PERSEGI PANJANG':^40}")
# print(f"{'-'*40:^40}")

# LEBAR = int(input("masukan nilai lebar : "))
# PANJANG = int(input("masukan nilai panjang : "))

# LUAS = PANJANG * LEBAR
# KELILING = 2*(PANJANG + LEBAR)

# print(f"hasil perhitungan luas = {LUAS}")
# print(f"hasil perhitungan keliling = {KELILING}")

def header():
    os.system('cls')

    print(f"{'PROGRAM MENGHITUNG LUAS':^40}")
    print(f"{'DAN KELILING PERSEGI PANJANG':^40}")
    print(f"{'-'*40:^40}")

def input_user():
    '''fungsi input user'''
    # mengambil input user
    lebar = int(input("Masukan nilai lebar : "))
    panjang = int(input("Masukan nilai panjang : "))

    return lebar, panjang

def hitung_luas(lebar, panjang):
    '''fungsi hitung luas'''
    return lebar * panjang

def hitung_keliling(lebar, panjang):
    '''fungsi hitung keliling'''
    return 2 * (lebar + panjang)

def display(message, value):
    '''fungsi display'''
    print(f"Hasil perhitungan {message} = {value}")

while True:
    header()

    LEBAR, PANJANG = input_user()
    LUAS = hitung_luas(LEBAR, PANJANG)
    KELILING = hitung_keliling(LEBAR, PANJANG)

    display("Luas", LUAS)
    display("Keliling", KELILING)

    isContinue = input("apakah lanjut (y/n)? ")
    if isContinue == "n":
        break

print("Program selesai, terima kasih")

