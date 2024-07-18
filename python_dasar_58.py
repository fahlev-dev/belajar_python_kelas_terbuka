'''menggunakan standar library'''

import datetime

data_waktu = datetime.datetime.now()
print(f"data waktu sekarang = {data_waktu}")
print(f"tahun sekarang = {data_waktu.year}")
print(f"Hari sekarang = {data_waktu.strftime('%A')}")

from collections import Counter

data = ["a","b","c","d","a","d","e"]
data_count = Counter(data)

print(f"data count = {data_count}")
print(f"jumlah a = {data_count['a']}")
print(f"jumlah d = {data_count['d']}")

import io

file = io.open('file_text.txt', 'r')
print(file.read())