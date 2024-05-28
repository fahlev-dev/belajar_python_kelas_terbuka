# continue, pass, break 

# pass -> dia berfungsi sebagai dummy, tidak akan di eksekusi 

# angka = 0 

# while angka < 5:
#     angka += 1

#     if angka == 3:
#         pass

#     print(angka)

# continue

angka = 0

print(f"angka yang sekarang -> {angka}")

while angka < 5:
    angka += 1
    print(f"angka sekarang -> {angka}")

    if angka == 3:
        print("Nice")
        continue # membuat loop loncat ke awal pengulangan

    print("Whatsapp")

print("Finish")