import datetime as dt

print("Silahkan masukan tanggal, bulan, dan tahun lahir anda :")

tanggal = int(input("Tanggal \t: "))
bulan = int(input("Bulan \t\t: "))
tahun = int(input("Tahun \t\t: "))

tanggal_lahir = dt.date(tahun, bulan, tanggal)
print(f"tanggal lahir anda adalah : {tanggal_lahir}")
print(f"hari nya adalah : {tanggal_lahir:%A}")

hari_ini = dt.date.today()
print(f"hari ini tanggal : {hari_ini}")
umur_hari = hari_ini - tanggal_lahir
umur_tahun = umur_hari.days // 365
umur_bulan_sisa = (umur_hari.days % 365) // 30
print(f"umur anda adalah : {umur_tahun} tahun, {umur_bulan_sisa} bulan")