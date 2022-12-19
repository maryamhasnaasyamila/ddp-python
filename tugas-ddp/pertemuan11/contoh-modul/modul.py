import math

def tambah(angka1, angka2):
    hasil = angka1 + angka2
    print("hasil dari ", angka1, "+", angka2, " = ", hasil)

def kurang(angka1, angka2):
    hasil = angka1 - angka2
    print("hasil dari ", angka1, "-", angka2, " = ", hasil)

def bagi(angka1, angka2):
    hasil = angka1 / angka2
    print("hasil dari ", angka1, ":", angka2, " = ", hasil)

def kali(angka1, angka2):
    hasil = angka1 * angka2
    print("hasil dari ", angka1, "x", angka2, " = ", hasil)

def pangkat(angka1, angka2):
    hasil = math.pow(angka1, angka2)
    print("hasil dari ", angka1, "^", angka2, " = ", hasil)