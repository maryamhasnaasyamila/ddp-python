# NO 1 - nilai yang lulus
hasil_akhir = [
    {'nama':'Reza', 'nilai':70},
    {'nama':'Ciut', 'nilai':63},
    {'nama':'Dian', 'nilai':80},
    {'nama':'Badu', 'nilai':40}
]

def lulus_saja(hasil_akhir):
    for x in hasil_akhir:
        if x['nilai'] > 65:
            lulus = x['nama']
            print(lulus, end=" ")
lulus_saja(hasil_akhir)

# NO 2 - membalikkan nilai
buah = [
  'Pepaya', 'Mangga', 'Pisang', 'Durian', 'Jambu',
]

for list_buah in reversed(buah):
  print(list_buah)


# NO 3 - duplikat buah
list_buah = [
    'pepaya', 'mangga', 'pisang','durian', 'jambu'
]

def buah():
    list_buah.insert(0, 'Pepaya')
    list_buah.insert(2, 'Mangga')
    list_buah.insert(4, 'Pisang')
    list_buah.insert(6, 'Durian')
    list_buah.insert(8, 'Jambu')
    print(list_buah)
buah()


# NO 4 - huruf konsonan
judul = "Nurul Fikri"
print(judul[0:10:2], end="r")