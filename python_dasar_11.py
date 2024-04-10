# belajar operator boolean 

# NOT
print("="*10, "NOT", "="*10)
a = True
c = not a

print("data a = ", a)

print("="*10, "NOT")
print("data c = ", c)

# OR
print("="*10, "OR", "="*10)
a = False
b = False
c = a or b
print(a, "OR", b, "=", c)
a = False
b = True
c = a or b
print(a, "OR", b, "=", c)
a = True
b = False
c = a or b
print(a, "OR", b, "=", c)
a = True
b = True
c = a or b
print(a, "OR", b, "=", c)

# AND
print("="*10, "AND", "="*10)
a = False
b = False
c = a and b
print(a, "and", b, "=", c)
a = False
b = True
c = a and b
print(a, "and", b, "=", c)
a = True
b = False
c = a and b
print(a, "and", b, "=", c)
a = True
b = True
c = a and b
print(a, "and", b, "=", c)

# XOR
print("="*10, "xor", "="*10)
a = False
b = False
c = a ^ b
print(a, "xor", b, "=", c)
a = False
b = True
c = a ^ b
print(a, "xor", b, "=", c)
a = True
b = False
c = a ^ b
print(a, "xor", b, "=", c)
a = True
b = True
c = a ^ b
print(a, "xor", b, "=", c)

