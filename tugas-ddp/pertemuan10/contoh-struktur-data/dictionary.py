# dictionary = menyimpan data bukan dengan index
# data disimpan sebagai key and value

data_diri = {
    "nama":"Hasna",
    "matpel":"DDP"}

data_diri["semester"] = 1
print(data_diri["nama"])

# mengakses dengan key
x = data_diri['nama']
# atau
x = data_diri.get('nama')

# mengubah value
data_diri['nama'] = "Hasna"

# menambah entri
data_diri['alamat'] = "Jakarta"

# menghapus key
data_diri.pop('alamat')

# mengecek keberadaan key dengan operator in
if('nama' in data_diri):
    print('nama ada di data_diri')