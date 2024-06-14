# copy dan pop dictionary

teman_teman = {
    "cup":"ucup surucup",
    "tong":"otong surotong",
    "dung":"dudung surudung",
    "sep":"asep surasep",
    "cuy":"ucuy surucuy"
}

friends = teman_teman.copy()

print(f"teman-teman : {teman_teman}\n")
print(f"friends: {friends}\n")

teman_teman["cup"] = "ucup si keren"
print(f"teman-teman : {teman_teman}\n")
print(f"friends: {friends}\n")

# pop dictionary ambil berdasarkan key
dataAsep = friends.pop("sep")
print(f"dataAsep = {dataAsep}")
print(f"friends: {friends}\n")

# pop item ambil berdasarkan data terkahir
dataTerakhir = friends.popitem()
print(f"data terkahir = {dataTerakhir}")
print(f"friends: {friends}\n")

