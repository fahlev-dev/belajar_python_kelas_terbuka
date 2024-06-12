# looping dictionary

teman_teman = {
    "cup":"ucup surucup",
    "tong":"otong surotong",
    "dung":"dudung surudung",
    "sep":"asep surasep",
    "cuy":"ucuy surucuy"
}

for teman in teman_teman:
    print(teman)

keys = teman_teman.keys()
print(keys)

for key in teman_teman.keys():
    print(teman_teman.get(key))

values = teman_teman.values()
print(values)

for value in teman_teman.values():
    print(value)

item = teman_teman.items()
print(item)

for item in teman_teman.items():
    print(item)

for key, value in teman_teman.items():
    print(f"key = {key}, value = {value}")