# NO.1 - PROGRAM HITUNG LUAS MENGGUNAKAN IMPORT MODUL BANGUN DATAR (yang dibuat sendiri)

print()
print("Program Mengihtung Luas Bangun Datar")
print("------------------------------------")
import modulbangundatar as mbd

print("Jajar Genjang")
mbd.jajarGenjang(int(input("Nilai alas: ")), int(input("Nilai tinggi: ")))
print()

print("Persegi")
mbd.persegi(int(input("Nilai sisi: ")))
print()
print("Persegi Panjang")
mbd.persegi_panjang(int(input("Nilai panjang: ")), int(input("Nilai lebar: ")))
print()

print("Lingkaran (phi = 3.14)")
mbd.lingkaran(int(input("Nilai r: ")))
print()

print("Layang-layang")
mbd.layang_layang(int(input("Nilai diagonal 1: ")), int(input("Nilai diagonal 2: ")))


