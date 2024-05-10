# operator dalam bentuk method

# uppercase
salam = "bro!"
print("normal = " + salam)
salam = salam.upper()
print("upper = " + salam)

# lowercase

kata = "INI ADALAH SEBUAH KATA"
print("normal = " + kata)
kata = kata.lower()
print("lower = " + kata)

salam = "ini adalah salam"
apakah_lower = salam.islower()
print(salam + " is lower = " + str(apakah_lower))
apakah_upper = salam.isupper()
print(salam + " is upper = " + str(apakah_upper))

# isalpha() untuk mengecek semuanya adalah huruf
# isalnum() untuk huruf dan angka
# isdecimal() untuk angka aja
# isspace() spasi, tab, dan newline
# istitle() untuk semua kata di mulai dengan huruf besar

kata = "alpha"
apakah_alpha = kata.isalpha()
print(kata + " is alpha = " + str(apakah_alpha))

kata = "ininomer10"
apakah_isalnum = kata.isalnum()
print(kata + " is alnum = " + str(apakah_isalnum))

cek_decimal = "10"
apakah_decimal = cek_decimal.isdecimal()
print(cek_decimal + " is decimal = " + str(apakah_decimal))

cek_space = " "
apakah_space = cek_space.isspace()
print(cek_space + " is space = " + str(apakah_space))

cek_title = "Hello World"
apakah_title = cek_title.istitle()
print(cek_title + " is title = " + str(apakah_title))

cek_start = "Sangjangnim Oppa".startswith("Sangjangnim")
print("start = " + str(cek_start))

cek_end = "Sangjangnim Oppak".endswith("Oppak")
print("end = " + str(cek_end))

pisah = ['aku', 'sayang', 'kamu']
gabungan = ','.join(pisah)
print(gabungan)

gabungan = ' '.join(pisah)
print(gabungan)

gabungan = 'akuehmsayangehmkamu'
print(gabungan.split('ehm')) # jadi list kembali

kanan = "kanan".rjust(10)
print("'" + kanan + "'")

kiri = "kiri".ljust(10)
print("'" + kiri + "'")

tengah = "tengah".center(10,"-")
print("'" + tengah + "'")

