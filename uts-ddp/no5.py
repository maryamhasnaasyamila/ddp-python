# MARYAM HASNAA' SYAMILA - ROMBEL TI03 - NIM 0110222067

print("<<** Program Kalkulator Sederhana **>>")
a = float(input("Masukkan Angka Pertama: "))
b = float(input("Masukkan Angka Kedua: "))
o = input("Pilih Operator (tambah/bagi/kurang/kali/pangkat): ")

if o == "tambah" or o == "Tambah" or o == "+" :
    hasil = (a+b)
    hasil2 = (b+a)
    print("==> Penyelesaian <==")
    print(a,"+",b,"=",a+b)
    print(b,"+",a,"=",b+a)
elif o == "kurang" or o == "Kurang" or o == "-":
    hasil = (a-b)
    hasil2 = (b-a)
    print("==> Penyelesaian <==")
    print(a,"-",b,"=",a-b)
    print(b,"-",a,"=",b-a)
elif o == "kali" or o == "Kali" or o == "*" : 
    hasil = (a*b)
    hasil2 = (b*a)
    print("==> Penyelesaian <==")
    print(a,"*",b,"=",a*b)
    print(b,"*",a,"=",b*a)
elif o == "bagi" or o == "Bagi" or o == "/" : 
    hasil = (a/b)
    hasil2 = (b/a)
    print("==> Penyelesaian <==")
    print(a,"/",b,"=",a/b)
    print(b,"/",a,"=",b/a)
elif o == "pangkat" or o == "Pangkat" or o == "**": 
    hasil = (a**b)
    hasil2 = (b**a)
    print("==> Penyelesaian <==")
    print(a,"**",b,"=",a**b)
    print(b,"**",a,"=",b**a)
else: 
    print("Operator tidak tersedia")

print()
print("==> Detail Output <==")
print("Angka Pertama:",a)
print("Angka Kedua:",b)
print("Pilihan Operator:",o)
print("Hasil:",hasil,"dan/atau",hasil2)