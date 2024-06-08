# teknik menduplikat list

a = ["ucup", "otong", "dudung"]
print(f"a = {a}")

b = a
print(f"b = {b}")

# akan merubah kedua list
a[1] = "michael"
b.sort()

print(f"a = {a}")
print(f"b = {b}")

# address kedua list a dan b
print(f"address a = {hex(id(a))}")
print(f"address b = {hex(id(b))}")

print(f"membuat list c dengan a.copy()")
c = a.copy()
print(f"address a = {hex(id(a))}")
print(f"address b = {hex(id(b))}")
print(f"address c = {hex(id(c))}")

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")

print("Kita ubah data index ke 0")
c[0] = "dadang"

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")

print("Kita ubah data index ke 1")
a[1] = "otong"

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")

