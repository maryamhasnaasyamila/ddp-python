# Program Logika If untuk Menghitung Nilai

nama = input("Nama = ")
kelas = input("Kelas = ")
nilai = float(input("Nilai = "))
if nilai >= 90 and nilai <= 100 :
    print("Ket = Istimewa")
elif nilai >= 70 and nilai <= 89 :
    print("Ket = Sangat Bagus")
elif nilai >= 60 and nilai <= 69 :
    print("Ket = Cukup")
else :
    print("Ket = Gagal")


