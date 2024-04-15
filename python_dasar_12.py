# input_user = int(input("masukan angka kurang dari 3 atau lebih besar dari 10: "))

# is_kurang_dari = (input_user < 3)

# print("kurang dari 3 =",is_kurang_dari)

# is_lebih_dari = (input_user > 10)

# print("lebih dari 10 =", is_lebih_dari)

# isCorrect = is_kurang_dari or is_lebih_dari

# print("angka yang dimasukan :", isCorrect)

# input_user = int(input("masukan angka lebih dari 3 dan kurang dari dari 10: "))

# is_lebih_dari = (input_user > 3)

# print("lebih dari 3 =",is_lebih_dari)

# is_kurang_dari = (input_user < 10)

# print("kurang dari 10 =", is_kurang_dari)

# isCorrect = is_lebih_dari and is_kurang_dari

# print("angka yang dimasukan :", isCorrect)

input_user = int(input("masukan angka lebih dari 0 kurang dari 5 dan lebih dari 8 kurang dari 11: "))

is_lebih_dari_0_kurang_dari_5 = (input_user > 0 and input_user < 5)

print("lebih dari 3 =",is_lebih_dari_0_kurang_dari_5)

input_user = int(input("masukan angka lebih dari 0 kurang dari 5 dan lebih dari 8 kurang dari 11: "))

is_lebih_dari_8_kurang_dari_11 = (input_user > 8 and input_user < 11)

isCorrect = is_lebih_dari_0_kurang_dari_5 and is_lebih_dari_8_kurang_dari_11

print("hasilnya adalah = ", isCorrect)

input_user = int(input("masukan angka kurang dari 0 atau lebih dari 5 atau kurang dari 8 atau lebih dari 11: "))

is_kurang_dari_0 = (input_user < 0)

input_user = int(input("masukan angka kurang dari 0 atau lebih dari 5 atau kurang dari 8 atau lebih dari 11: "))

is_lebih_dari_5_kurang_dari_8 = (input_user > 5 and input_user < 8)

input_user = int(input("masukan angka kurang dari 0 atau lebih dari 5 atau kurang dari 8 atau lebih dari 11: "))

is_lebih_dari_11 = (input_user > 11)

isCorrect = is_kurang_dari_0 or is_lebih_dari_5_kurang_dari_8 or is_lebih_dari_11

print("hasilnya adalah = ", isCorrect)