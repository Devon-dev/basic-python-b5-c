#type1
def func_luas_persegi(p,l):
    Luas = p*l
    return Luas
#type2
def func_keliling_persegi(p,l):
    return p+p+l+l
#type3
def hitung_luas_keliling_persegi(p,l):
    luas = p*l
    keliling = p+p+l+l
    return luas,keliling

luas = func_luas_persegi(10,5)
print(luas)

keliling = func_keliling_persegi(10,5)
print(keliling)

luas_keliling = hitung_luas_keliling_persegi(10,5)
LUAS    = luas_keliling[0]   #tampilkan luas hitung bangun
KLILING = luas_keliling[1]   #tampilkan keliling hitung bangun
# display 1
print(LUAS)
print(KLILING)
# display 2
for i in luas_keliling:
    print(i)