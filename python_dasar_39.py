# operasi dictionary

data_dict = {
    'cup':'ucup surucup',
    'tong':'otong surotong',
    'dung':'dadang sududung'
}

LENDICT = len(data_dict)
print(f"panjang dictionary : {LENDICT}")

# mengecek key exist atau tidak
KEY = "cup"
CHECK_KEY = KEY in data_dict
print(f"apakah {KEY} ada di data dict: {CHECK_KEY}")

print(data_dict["cup"])
print(data_dict.get("cup"))
print(data_dict.get("kis","key tidak ditemukan")) # cek key dengan message tidak di temukan

# update data
data_dict["cup"] = "ucup si ganteng"
print(data_dict)
data_dict["sep"] = "Asep si kasep"
print(data_dict)

data_dict.update({"cup":"ucup surucup"})
print(data_dict)
data_dict.update({"faqih":"faqihza si ganteng"})
print(data_dict)

# menghapus data pada dictionary
del data_dict["faqih"]
print(data_dict)