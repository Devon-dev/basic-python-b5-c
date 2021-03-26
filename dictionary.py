#make array
thisdict = {                         #dictionary
    "brand" : "Ford",
    "model" : "Mustang",
    "year"  : 1964
}
thislist = ["Ford", "Mustang", 1964] #list

#display all
print(thisdict) #dictionary
print(thislist) #list

#change value
thisdict["year"] = 2018 #dictionary
thislist[2] = 2020      #list

#accessing items
print(thisdict["year"]) #dictionary
print(thislist[2])      #list

#display all
print(thisdict) #dictionary
print(thislist) #list

#loop display dictionary
for x in thisdict:
    print(x)

#tambah key baru
thisdict["harga"] = 2000000
print(thisdict)