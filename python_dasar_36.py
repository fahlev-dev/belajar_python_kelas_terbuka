# program list buku 

list_buku = []
while True:
    print("\nMasukan data buku")
    judul = input("Judul buku \t: ")
    penulis = input("Penulis buku \t: ")

    buku_baru = [judul, penulis]
    list_buku.append(buku_baru)

    print("\n\n","="*10, "Data Buku", "="*10)
    for index, buku in enumerate(list_buku):
        print(f"{index+1} | {buku[0]} | {buku[1]}")

    tambah_buku = input("Apakah ingin menambahkan buku (y/t) : ")

    if tambah_buku == "t":
        break

print("akhir aplikasi")