#input
ubin1=int(input("Masukkan jumlah ubin 1 meter: "))
ubin5=int(input("Masukkan jumlah ubin 5 meter: "))
panjang=int(input("Masukkan panjang yang ingin ditutupi ubin: "))

#cek panjang total
if (1*ubin1 +5*ubin5)>= panjang:
    #berarti mungkin bisa
    #cek apakah cukup pakai ubin
    if panjang%5==0 and panjang//5<= ubin5 
        print ("bisa")
    elif panjang//5<= ubin5 and panjang%5<=ubin1:
        print ("bisa")
    else:
        print ("tidak bisa")
else:
    print("tidak bisa")