# Exception, Error, Try, dan Except

# input_angka = int(input("masukan angka : "))

# hasil = 10 / input_angka

# print(hasil)

# from math import nan

# input_angka = int(input("masukan angka : "))
# hasil = nan

# try:
#     hasil = 10 / input_angka
# except:
#     print("input tidak boleh 0")

# print(f"hasil = {hasil}")

# while(True):
#     angka = int(input("masukan angka : "))
#     try:
#         hasil = 10 / angka
#         print(f"hasil = {hasil}")
#         is_done = input("Lanjutkan (y/n) : ")
#         if is_done == "n":
#             break
#     except:
#         print("input tidak boleh 0")

# print("akhir program")

# while(True):
#     try:
#         with open("data.txt", mode="r") as file:
#             print(file.read())
#         break
#     except:
#         print("file data.txt tidak ditemukan, membuat file kembali")
#         with open("data.txt", mode="w") as file:
#             file.write("data file txt baru")
#         break

# print("akhir dari program")

# from numbers import Number

# def tambah(a,b):
#     if not isinstance(a, Number) or not isinstance(b, Number):
#         raise "input harus angka"
#     return a + b

# print(tambah(5,6))

angka = 0

try:
    hasil = 10 / angka
except Exception as error_message:
    print(error_message)



