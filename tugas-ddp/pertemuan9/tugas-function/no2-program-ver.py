# Nama : Maryam Hasnaa' Syamila
# Kelas : TI03
# NIM : 0110222067

# SOAL NO 3 - CUACA (prgram ver.)
print()
print("program if elif cuaca beserta keterangannya")
print("===========================================")

def keterangan(cuaca = input("Kondisi cuaca: ")): 
    if cuaca == "hujan" or cuaca == "Hujan"  or cuaca == "HUJAN" :
        print("Ket: naik gocar")
    elif cuaca == "adem" or cuaca == "Adem"  or cuaca == "ADEM" :
        print("Ket: naik motor")
    else :
        print("Ket: tidak jadi berangkat")
keterangan()