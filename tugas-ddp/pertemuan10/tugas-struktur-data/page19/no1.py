# Siswa yang lulus dengan nilai > 95

hasilAkhir = [
    {'nama':'Reza', 'nilai_siswa':70},
    {'nama':'Ciut', 'nilai_siswa':63},
    {'nama':'Dian', 'nilai_siswa':80},
    {'nama':'Badu', 'nilai_siswa':40}
]

def lulus_saja(hasilAkhir):
    siswa_lulus = []
    for x in hasilAkhir:
        if x['nilai_siswa'] > 65:
            siswa_lulus.append(x['nama'])
    print(siswa_lulus, end=" ")
lulus_saja(hasilAkhir)

