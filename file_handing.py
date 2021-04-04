# append
f open("nama txt", "a")
f.write("Diki\n")
f.write("Joni\n")
f.write("Navi\n")
f.write("Bmbang\n")
f.close()

# write
f = open("nama.txt","a")
f.write("Hello!\n")
f.write("Namaku Nafi\n")
f.write("Umurku 22!\n")

f.close()

# read
f = open("nama.txt", "r")

# menulis secara keseluruhan
# print(f.read())

# cek type data
# data = f.read()
# print(type(data))

# menulis secara part/batas tertu
# print(f.read(5))

# dibaca perline/perbaris
print(f.readline())