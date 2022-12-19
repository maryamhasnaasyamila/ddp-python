# NO.1 - MODUL BANGUN DATAR UNTUK MENGHITUNG LUAS [min. 5]

import math
def persegi(s):
    luas = math.pow(s, 2)
    print("Luas persegi: ", luas)

def persegi_panjang(p, l):
    luas = p * l
    print("Luas persegi panjang: ", luas)

def lingkaran(r):
    luas = 3.14 * math.pow(r, 2)
    print("Luas lingkaran: ", luas)

def jajarGenjang(a, t):
    luas = a * t
    print("Luas jajar genjang: ", luas)

def layang_layang(d1, d2):
    luas = 1/2 * d1 * d2 
    print("Luas layang-layang: ", luas)

def trapesium(sa, sb, t):
    luas = 1/2 * t * (sa + sb)
    print("Luas trapesium: ", luas)

def segitiga(a, t):
    luas = a * t
    print("Luas segitiga: ", luas)

def belahKetupat(d1, d2):
    luas = 1/2 * d1 * d2 
    print("Luas belah ketupat: ", luas)