# NO.1 - PROGRAM MENGHITUNG LUAS BANGUN DATAR DENGAN IF ELSE & MODUL
print()

bd = input("Bangun Datar: ")
if bd == "jajar genjang" or bd == "Jajar Genjang" or bd == "Jajar genjang" or bd == "JAJAR GENJANG":
    import modulbangundatar as mbd
    mbd.jajarGenjang(int(input("Nilai alas: ")), int(input("Nilai tinggi: ")))

elif bd == "persegi" or bd == "Persegi" or bd == "PERSEGI":
    import modulbangundatar as mbd
    mbd.persegi(int(input("Nilai sisi: ")))

elif bd == "persegi panjang" or bd == "Persegi panjang" or bd == "Persegi Panjang" or bd == "PERSEGI PANJANG":
    import modulbangundatar as mbd
    mbd.persegi_panjang(int(input("Nilai panjang: ")), int(input("Nilai lebar: ")), int(input("Nilai tinggi: ")))

elif bd == "lingkaran" or bd == "Lingkaran" or bd == "LINGKARAN":
    import modulbangundatar as mbd
    mbd.lingkaran(int(input("Nilai r: ")))

elif bd == "layang-layang" or bd == "Layang-layang" or bd == "Layang-Layang" or bd == "LAYANG-LAYANG":
    import modulbangundatar as mbd
    mbd.layang_layang(int(input("Nilai diagonal 1: ")), int(input("Nilai diagonal 2: ")))

elif bd == "belah ketupat" or bd == "Belah Ketupat" or bd == "Belah ketupat" or bd == "BELAH KETUPAT":
    import modulbangundatar as mbd
    mbd.belahKetupat(int(input("Nilai diagonal 1: ")), int(input("Nilai diagonal 2: ")))

elif bd == "trapesium" or bd == "Trapesium" or bd == "TRAPESIUM":
    import modulbangundatar as mbd
    mbd.trapesium(int(input("Nilai tinggi: ")), int(input("Nilai sisi atas: ")), int(input("Nilai sisi bawah: ")))

elif bd == "segitiga" or bd == "Segitiga" or bd == "SEGITIGA":
    import modulbangundatar as mbd
    mbd.segitiga(int(input("Nilai alas: ")), int(input("Nilai tinggi: ")))

else: 
    print("Bangun datar yang Anda cari tidak terdata dimodul.")