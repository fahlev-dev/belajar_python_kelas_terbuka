# write eksternal file di python

# akan membuat file baru jika tidak ada lalu akan menimpa atau overwrite isinya

with open("data1.txt", mode="w", encoding="utf-8") as file:
    file.write("jon si jhonny")

with open("data1.txt", mode="a", encoding="utf-8") as file:
    file.write("\nucup surucup")

with open("data1.txt", mode="a", encoding="utf-8") as file:
    file.write("\ndi tambah lagi dengan parameter append")