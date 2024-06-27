'''fungsi dengan kembalian'''

def kuadrat(input_angka):
    '''fungsi kuadrat'''
    output_kuadrat = input_angka ** 2
    return output_kuadrat

y = kuadrat(10)
print(y)

print(kuadrat(11))

def fungsi_tambah(angka1, angka2):
    return angka1 + angka2

a = fungsi_tambah(10, 10)
print(a)

def opearasi_matematika(angka1, angka2):
    tambah = angka1 + angka2
    kurang = angka1 - angka2
    kali = angka1 * angka2
    bagi = angka1 / angka2

    return tambah, kurang, kali, bagi

k, l, m, n = opearasi_matematika(9, 5)

print(f"Hasil tambah = {k}")
print(f"Hasil kurang = {l}")
print(f"Hasil kali = {m}")
print(f"Hasil bagi = {n}")