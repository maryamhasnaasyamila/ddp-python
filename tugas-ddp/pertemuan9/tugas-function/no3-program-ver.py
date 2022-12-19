# Nama : Maryam Hasnaa' Syamila
# Kelas : TI03
# NIM : 0110222067

# SOAL NO 3 - BIODATA (program ver.)
print()
print("program menuliskan biodata diri")
print("===============================")

def biodata1(nama = input("Nama: "), alamat = input("Alamat: "), tglLahir = input("Tanggal lahir: "), umur = (input("Umur: "))):
    print(biodata1(nama))
    print(biodata1(alamat))
    print(biodata1(tglLahir))
    print(biodata1(umur))

def biodata2(tB = int(input("Tinggi badan: "))):
    return (tB-100)-((tB-100)*15/100)
print("Berat badan ideal: ", biodata2())
