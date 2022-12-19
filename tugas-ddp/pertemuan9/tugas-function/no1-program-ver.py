# Nama : Maryam Hasnaa' Syamila
# Kelas : TI03
# NIM : 0110222067

# SOAL NO 1 - PERS. LINEAR (program ver.)
print()
print("program menghitung persamaan linear dari x^2 + 7y - z")
print("====================================================")

def persamaanLinear(x = int(input("masukan nilai x = ")), y = int(input("masukan nilai y = ")), z = int(input("masukan nilai z = "))):
    return x**2+7*y-z

print("-------------------")
print("hasil = ", persamaanLinear())