DaftarAngka = [15, 25, 9, 19, 50, 33, 21]
 
length = len(DaftarAngka) - 1
sorted = False
 
while not sorted:
         sorted = True
         for i in range(length):
                   if DaftarAngka[i] > DaftarAngka[i+1]:
                   sorted = False
                   DaftarAngka[i], DaftarAngka[i+1] = DaftarAngka[i+1], DaftarAngka[i]
 
print DaftarAngka
