def maju(arah):
    if(arah == "kanan"):
        print("Maju ke ==>")
    elif(arah == "kiri"):
        print("Maju ke <==")
    else:
        print("Diam")

def rintangan(jenis_rintangan):
    if(jenis_rintangan =="batu"):
        print("Lompat ke atas")
    elif(jenis_rintangan =="burung"):
        print("Merunduk kebawah")

q = "start"
while q != "leave":
    print("Jika ada sungai dikananmu kemana kamu pergi ?")
    print("Tentukan langkahmu :")
    print("1. Kekanan")
    print("2. Kekiri")
    jawab = int(input("Jawab ="))
    if(jawab == 1):
        maju("kanan")
        print("byur...")
    elif(jawab == 2):
        maju("kiri")
        print("selamat !...")
    print("========================")
    q = input("Mau lanjut ?")