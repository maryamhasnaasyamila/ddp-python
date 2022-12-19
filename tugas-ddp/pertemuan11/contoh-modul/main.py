import modul
modul.tambah(3, 4)
modul.kali(12, 3)
modul.bagi(45, 9)
modul.kurang(99-33)

# import dengan penyingkatan
import modul as m
m.tambah(3, 4)
m.kali(12, 3)
m.bagi(45, 9)
m.kurang(99-33)

# import dengan form
from modul import *
modul.tambah(5, 5)
modul.kali(6, 6)
modul.bagi(15, 3)
modul.kurang(20-5)


# import dengan form dengan penyingkatan
from modul import tambah as plus, kurang as min, bagi as div, kali as x  
plus.tambah(5, 5)
x.kali(6, 6)
div.bagi(15, 3)
min.kurang(20-5)