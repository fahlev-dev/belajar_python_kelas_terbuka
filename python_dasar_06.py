# casting tipe data 

data_int = 10
print("data = ", data_int, " type = ", type(data_int))

data_float = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int) # akan False jika nilai integer 0

print("data = ", data_float, " type = ", type(data_float))
print("data = ", data_str, " type = ", type(data_str))
print("data = ", data_bool, " type = ", type(data_bool))

print("===================================================================")

data_float = 10.5
print("data = ", data_float, " type = ", type(data_float))

data_int = int(data_float)
data_str = str(data_float)
data_bool = bool(data_float) # akan False jika nilai integer 0

print("data = ", data_int, " type = ", type(data_int))
print("data = ", data_str, " type = ", type(data_str))
print("data = ", data_bool, " type = ", type(data_bool))

print("===================================================================")

data_bool = True
print("data = ", data_bool, " type = ", type(data_bool))

data_int = int(data_bool)
data_str = str(data_bool)
data_float = float(data_bool) # akan False jika nilai integer 0

print("data = ", data_int, " type = ", type(data_int))
print("data = ", data_str, " type = ", type(data_str))
print("data = ", data_float, " type = ", type(data_float))

print("===================================================================")

data_str = "Mukidi"
print("data = ", data_str, " type = ", type(data_str))

data_int = int(data_str)
data_bool = bool(data_str)
data_float = float(data_str) # akan False jika nilai integer 0

print("data = ", data_int, " type = ", type(data_int))
print("data = ", data_bool, " type = ", type(data_bool))
print("data = ", data_float, " type = ", type(data_float))
