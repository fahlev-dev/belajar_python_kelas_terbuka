data_integer = 10 # angka satuan yang tidak ada koma
print("data : ", data_integer, ", tipe ", type(data_integer))

data_float = 10.0 # angka yang ada koma
print("data : ", data_float, ", tipe ", type(data_float))

data_string = "Ucup"
print("data : ", data_string, ", tipe ", type(data_string))

data_bool = True
print("data : ", data_bool, ", tipe ", type(data_bool))

data_complex = complex(5, 6)
print("data : ", data_complex, ", tipe ", type(data_complex))

from ctypes import c_double

data_c_double = c_double(10.5)
print("data : ", data_c_double, ", tipe ", type(data_c_double))
