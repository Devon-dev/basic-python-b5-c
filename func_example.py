def func_luas_persegi(p,l):
    Luas = p*l
    return Luas

def func_keliling_persegi():
    p = int(input("Masukkan panjang : "))
    l = int(input("Masukkan lebar : "))
    return p+p+l+l

while True:
    print("l - Luas")
    print("k - Keliling")
    print("exit - Keluar Program")
    tanya = str(input("Masukkan Pilihan : "))
    if tanya == "l":
        p = int(input("Masukkan panjang : "))
        l = int(input("Masukkan lebar : "))
        print("Hasil luasnya adalah :",func_luas_persegi(p,l))
    elif tanya == "k":
        print("Kelilingnya adalha",func_keliling_persegi())
    elif tanya == "exit":
        break
    else:
        print("Masukkan pilihan yang benar!")
        print("=============================")

    tanya2 = str(input("Ulangi sekali lagi ? "))
    if tanya2 == "y" :
        continue
    else:
        break