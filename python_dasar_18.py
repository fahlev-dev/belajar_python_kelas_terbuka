nama = "marlene"
format_str = f"hello {nama}"

print(format_str)

angka = 2005.5
format_str = f"angka = {angka}"
print(format_str)

boolean = True
format_str = f"boolean = {boolean}"
print(format_str)

angka = 15
format_str = f"bilangan bulat = {angka}"
print(format_str)

angka = 2000000
format_str = f"jutaan = {angka:,}"
print(format_str)

angka = 2005.54321
format_str = f"desimal = {angka:.3f}"
print(format_str)

angka_minus = -10
angka_plus = 10.1234
format_minus = f"minus = {angka_minus:+d}"
format_plus = f"plus = {angka_plus:+.2f}"

print(format_minus)
print(format_plus)

persentase = 0.045
format_persen = f"persen = {persentase:.2%}"
print(format_persen)

harga = 10000
jumlah = 5

format_string = f"harga total = Rp.{harga * jumlah:,}"
print(format_string)

angka = 255
format_binary = f"binary = {bin(angka)}"
format_octal = f"octal = {oct(angka)}"
format_hex = f"hex = {hex(angka)}"

print(format_binary)
print(format_octal)
print(format_hex)