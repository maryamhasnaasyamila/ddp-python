# Program Logika If untuk Praktikum

Lab = input("Kondisi Lab = ")
if Lab == "tersedia" or Lab == "ada" or Lab == "baik" :
    print("Ket = praktikum")
elif Lab == "penuh" or Lab == "dipakai" :
    print("Ket = pindah jadwal")
else :
    print("Ket = tidak jadi praktikum")