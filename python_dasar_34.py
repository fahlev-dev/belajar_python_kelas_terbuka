# deep copy nested list

data_0 = [1,2]
data_1 = [3,4]

data_2D = [data_0, data_1]
data_2D_copy = data_2D.copy()

print(f"data = {data_2D}")
print(f"data = {data_2D_copy}")

# mengambil data di nested list
data = data_2D[0][0]

print(f"data = {data}")

print(f"address data_2D = {hex(id(data_2D))}")
print(f"address data_2D_copy = {hex(id(data_2D_copy))}")

print("address dari member ke-1")
print(f"address data_2D = {hex(id(data_2D[0]))}")
print(f"address data_2D_copy = {hex(id(data_2D_copy[0]))}")

from copy import deepcopy

data_2D = [data_0, data_1, 10]
data_2D_deepcopy = deepcopy(data_2D)

print(f"address data_2D = {hex(id(data_2D))}")
print(f"address data_2D_copy = {hex(id(data_2D_copy))}")

print(f"address data_2D = {hex(id(data_2D))}")
print(f"address data_2D_deepcopy = {hex(id(data_2D_deepcopy))}")
