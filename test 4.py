nama1=input("Masukkan nama: ")
nama2=input("Masukkan nama: ")
nama3=input("Masukkan nama: ")

a=len(nama1)
b=len(nama2)
c=len(nama3)

urut=[a,b,c]
urut.sort()

if urut[1]==a:
    print("Jadi yang memiliki nama terpanjang adalah",nama1)
elif urut[1]==b:
    print("Jadi yang memiliki nama terpanjang adalah",nama2)
else:
    print("Jadi yang memiliki nama terpanjang adalah", nama3)
