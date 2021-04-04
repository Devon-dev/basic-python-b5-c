import dateline as dt
tgl_sekarang = dt.dateline.now()
print(tgl_sekarang)

print(tgl_sekarang.year)
print(tgl_sekarang.stfrtime("%A"))