print()
print("===== Program Pemesanan di Restaurant =====")
nama = input("Nama Pembeli = ")
notelp = input ("No. HP = ")
menu = input("Daftar Menu (Makanan/Minuman)  = ")

if menu == "makanan" or menu == "Makanan" or menu == "MAKANAN" :
    print("""
    ====== Menu Makanan =======
    1. Nasi Goreng = Rp15.000
    2. Mie Goreng = Rp12.000
    3. Ayam Geprek = Rp18.000
    """)
elif menu ==  "minuman" or menu == "Minuman" or menu == "MINUMAN" :
    print("""
    ======= Menu Minuman =======
    4. Aneka Jus = Rp. 15.000
    5. Soft Drink = Rp. 10.000
    6. Sweet Ice Tea = Rp. 5.000
    """)

print("***")
pesan = input("Masukkan Pesanan Anda = ")
jumlah = int(input("Jumlah Pesanan = "))

if pesan == "nasi goreng" or pesan == "Nasi Goreng" or pesan == "NASI GORENG" :
    harga = (15000*jumlah)
elif pesan == "mie goreng" or pesan == "Mie Goreng" or pesan == "MIE GORENG" :
    harga = (12000*jumlah)
elif pesan == "ayam geprek" or pesan == "Ayam Geprek" or pesan == "AYAM GEPREK" :
    harga = (18000*jumlah)
elif pesan == "aneka jus" or pesan == "Aneka Jus" or pesan == "ANEKA JUS" :
    harga = (15000*jumlah)
elif pesan == "soft drink" or pesan == "Soft Drink" or pesan == "SOFT DRINK" :
    harga = (10000*jumlah)
elif pesan == "sweet ice tea" or pesan == "Sweet Ice Tea" or pesan == "SWEET ICE TEA" :
    harga = (5000*jumlah)

print('''
===== Rincian Order ===== ''')
print("Nama: ", nama) 
print("No. HP: ", notelp)
print("Pesanan: ", pesan)
print("Jumlah: ", jumlah)
print("Total Tagihan: Rp.", harga)