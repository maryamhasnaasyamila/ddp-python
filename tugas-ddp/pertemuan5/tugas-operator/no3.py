#membuat program menghitung berat badan ideal

bb = float(input("masukan berat badan (kg) = "))
tb = float(input("masukan tinggi badan (cm) = "))

x = float(tb-100)
y = float(x*15/100)
ideal = (x-y)
print(ideal)