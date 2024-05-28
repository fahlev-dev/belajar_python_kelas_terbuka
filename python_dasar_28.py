sisi = 10

count = 1
for i in range(sisi):
    print("*" * count)
    count += 1

count = 1
while True:
    print("*" * count)
    count += 1

    if count > sisi:
        break

count = 1
while True:
    if (count % 2):
        print("*" * count)
        count += 1
    else:
        count += 1
        continue

    if count > sisi:
        break

