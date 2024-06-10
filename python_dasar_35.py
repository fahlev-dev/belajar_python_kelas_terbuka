# looping dari list

kumpulan_angka = [4,3,2,5,6,1]

for angka in kumpulan_angka:
    print(f"angka = {angka}")

print("\n for loop dan range")
peserta = ["ucup", "otong", "dadang", "diding", "dudung"]

for nama in peserta:
    print(f"nama = {nama}")

kumpulan_angka = [10, 4, 3, 2, 4, 5, 6, 5, 4, 3, 3, 2]

panjang_angka = len(kumpulan_angka)

for i in range(panjang_angka):
    print(f"angka = {kumpulan_angka[i]}")

print("\nwhile loop")

kumpulan_angka = [10, 4, 3, 2, 4, 5, 6, 5, 4, 3, 3, 2]

panjang_angka = len(kumpulan_angka)

i = 0

while i < panjang_angka:
    print(f"angka = {kumpulan_angka[i]}")
    i += 1

# list comprehension
print("\nlist comprehension")
data = ["ucup", 1, 2, 3, "otong"]

[print(f"data = {i}\n") for i in data]

kumpulan_angka = [10, 4, 3, 2, 4, 5, 6, 5, 4, 3, 3, 2]

angka_kuadrat = [i**2 for i in kumpulan_angka]
print(angka_kuadrat)

# enumerate
print("\nenumerate")
data_list = ["ucup", 1, 2, 3, "otong"]

for index, data in enumerate(data_list):
    print(f"index = {index}, data = {data}")

