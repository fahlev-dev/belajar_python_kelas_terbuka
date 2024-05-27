print(20*"=")
print("Kalkulator sederhana")
print(20*"=" + "\n")

angka_1 = float(input("Masukan angka 1: "))
operator = input("operator = (+, -, *, /): ")
angka_2 = float(input("Masukan angka 2: "))

if operator == "+":
    hasil = angka_1 + angka_2
    print(f"Hasilnya adalah : {hasil}")
elif operator == "-":
    hasil = angka_1 - angka_2
    print(f"Hasilnya adalah {hasil}")
elif operator == "x":
    hasil = angka_1 * angka_2
    print(f"Hasilnya adalah {hasil}")
elif operator == "/":
    if angka_1 == 0 or angka_2 == 0:
        print("Tidak bisa dibagi 0")
    hasil = angka_1 / angka_2
    print(f"Hasilnya adalah {hasil}")
else:
    print("Tidak ada operator")


