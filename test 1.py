#input
suhu=float(input("Masukkan suhu: "))

#demam atau tidak? jika demam maka >=38
if suhu >= 38.0 and suhu<=40.9:
    print("Deman")
if suhu <34.0:
    print("Mati Kedinginan")
if suhu>=34.0 and suhu<=37.9:
    print ("Aman")
if suhu >40.9:
    print("Mati Kepanasan")
else:
    print ("Tidak Demam")
