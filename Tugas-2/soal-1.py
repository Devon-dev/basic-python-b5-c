def func_nama
    no telepon = 08123456789
    return Luas

def func_keliling_persegi():
    p = int(input("Masukkan nama : "))
    l = int(input("Masukkan nomor telepon : "))
    return p+p+l+l

while True:
    print("n - nama")
    print("t - telepon")
    print("exit - Keluar Program")
    tanya = str(input("Masukkan Pilihan : "))
    if tanya == "l":
        p = int(input("Masukkan nama : "))
        l = int(input("Masukkan telepon : "))
        print("Hasil luasnya adalah :",func_nama
    elif tanya == "k":
        print("Kelilingnya adalha",func_nomor_telepon
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