# MARYAM HASNAA' SYAMILA - ROMBEL TI03 - NIM 0110222067

print("Program Menghitung Luas dan Keliling Layang-layang (cm)")
print("===================================================")
opsi = input("Mau Menghitung Luas (L) atau Keliling(K) Layang-layang?: ")
if opsi == "luas" or opsi == "Luas" or opsi == "L" or opsi == "l" :
    print("=> Menghitung Luas Layang-layang <=")
    print("[Rumus Luas: 1/2*d1*d2]")
    d1 = float(input("Masukan nilai Diagonal 1: "))
    d2 = float(input("Masukan nilai Diagonal 2: "))
    luas = (1/2)*d1*d2
    print("Luas:",luas,"cm")

elif opsi == "keliling" or opsi == "Keliling" or opsi == "k" or opsi == "K" :
    print("=> Menghitung Keliling Layang-layang <=")
    print("[Rumus Keliling: 2*(sisi miring pendek + sisi miring panjang)]")
    smk = float(input("Masukan nilai sisi miring pendek: "))
    smp = float(input("Masukan nilai sisi miiring panjang: "))
    keliling = 2*(smk + smp)
    print("Keliling:",keliling,"cm")