dimensional = []
kolom1 = [0, 1, 2]
kolom2 = [0, 1, 2]

for x in kolom1:
    dimensional.append(x)
    dimensional[x] = []
    for y in kolom2:
        dimensional[x].append(y)
        dimensional[x][y] = str(x) + ',' + str(y)

print(dimensional)
