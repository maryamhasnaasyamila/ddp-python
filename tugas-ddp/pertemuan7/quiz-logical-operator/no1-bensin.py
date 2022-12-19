print()
print("Program Perhitungan Pemakaian Bensin")
print("*************************************")
kendaraan = input("Jenis Kendaraan (Mobil/Motor) = ")
bensin = input("Jenis Bensin (Pertalite/Pertamax/Pertamax Turbo) = ")

if bensin == "Pertalite" or bensin == "pertalite" or bensin == "PERTALITE" :
    harga_bensin = 10000
    jarak_tempuh = 12
elif bensin == "Pertamax" or bensin == "pertamax" or bensin == "PERTAMAX" :
    harga_bensin = 13000
    jarak_tempuh = 13
elif bensin == "Pertamax Turbo" or bensin == "pertamax turbo" or bensin == "Pertamax turbo = " or bensin == "PERTAMAX TURBO = " :
    harga_bensin = 17000
    jarak_tempuh = 13.5
else :
    print("Not found, please try again.")
    exit()

kota = input("Kota yang Dituju (Jakarta/Bekasi/Depok/Tanggerang/Bogor) = ")
if kota == "Jakarta" or kota == "jakarta" or kota == "DKI Jakarta" or kota == "DKI JAKARTA" :
    jarak_kota = 20
elif kota == "Bekasi" or kota == "bekasi" or kota == "BEKASI" :
    jarak_kota = 35.7
elif kota == "Depok" or kota == "depok" or kota == "DEPOK" :
    jarak_kota = 5
elif kota == "Tanggerang" or kota == "tanggerang" or kota == "TANGGERANG" :
    jarak_kota = 99
elif kota == "Bogor" or kota == "bogor" or kota == "BOGOR" :
    jarak_kota = 120.6
else :
    print("Not found, please try again")
    exit()

PemakaianBensin = float(jarak_kota/jarak_tempuh)
TotalHargaBensin = int(PemakaianBensin*harga_bensin)

print()
print("Rincian")
print("********")
print("Jenis Kendaraan: ", kendaraan)
print("Jenis Bensin: ", bensin)
print("Kota Tujuan: ", kota)
print("Pemakaian Bensin = ", PemakaianBensin, "Liter")
print("Total Harga = Rp.", TotalHargaBensin)