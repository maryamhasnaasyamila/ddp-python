# mencari luas dan keliling jajar genjang

# luas jajar genjang
# rumus = alas kali tinggi
msg_luas = "Luas Jajar Genjang"
print(msg_luas)
alas = int(input("Masukan nilai alas: "))
tinggi = int(input("Masukan nilai tinggi: "))
l = alas * tinggi
print(l)

# keliling jajar genjang
# rumus = 2 kali (alas + sisi miring)
msg_keliling = "Keliling Jajar Genjang"
print(msg_keliling)
alas = int(input("Masukan nilai alas = "))
sisiMiring = int(input("Masukan nilai sisi miring = "))
k = 2 * (alas + sisiMiring)
print(k)