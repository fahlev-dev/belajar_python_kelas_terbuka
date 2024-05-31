# belajar list

# data number
data_angka = [1,2,3,4,5,6,7,8,9,10]
print(data_angka)

# data string
data_string = ["ucup", "otong", "janda"]
print(data_string)

# data boolean
data_boolean = [True, False, True, False]
print(data_boolean)

# data campuran 
data_campuran = ["ucup", 1, True, 4.5]
print(data_campuran)

data_list = list(range(0, 10))
print(data_list)

for_list = [i**2 for i in range(1, 11)]
print(for_list)

for_list_if = [i for i in range(0, 10) if i != 5]
print(for_list_if)

for_list_if_genap = [i for i in range(0, 10) if i % 2 == 0]
print(for_list_if_genap)

for_list_if_ganjil = [i for i in range(0, 10) if i % 2 == 1]
print(for_list_if_ganjil)