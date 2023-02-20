#input
cigars=int(input("Masukkan jumlah rokok: "))
weekend=input("Apakah weekend? (Y/N): ")

is_weekend = False

#proses
if weekend=='Y' or weekend=='y':
    is_weekend=True


if is_weekend ==True and cigars>=40:
    print("Sukses")
elif is_weekend == False and 40>=cigars<=60:
    print("Sukses")
else:
    print("Gagal")