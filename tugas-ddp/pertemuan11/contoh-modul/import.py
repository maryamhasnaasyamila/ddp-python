import math
print(math.pow(10, 2)) # pangkat
print(math.sqrt(121)) # akar
print(math.log(10)) # log 10
print(math.log10(1000)) # log dari kelipatan 10
print(math.fmod(7, 3)) # modulus (hasil sisa pembagian)

import datetime
print(datetime.datetime.now()) # menunjukkan waktu sekarang
print(datetime.datetime.now().year) # menujukkan waktu sekarang dalam tahun

seratus = datetime.datetime.now() + datetime.timedelta(days=100) # utk mengatahui tanggal brp 100 hari stlh hari ini
print(seratus.__str__())

# datetime menggunakan for & import
hari_ini = datetime.date.today
print(hari_ini.weekday) # ???