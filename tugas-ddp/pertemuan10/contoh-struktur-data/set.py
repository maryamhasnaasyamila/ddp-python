# set = himpunan 
# tdk ada duplikasi, tidak ada jaminan urutan

a = {6,5,4}
print(a)

# menambahkan = add
# menghapus = remove
a.add(3)
a.add(6)
a.remove(5)
print(a)
print(a.pop())
print(a)
print()

# menggabungkan dengan union
set1 = {1,2,3}
set2 = {2,4,6}
set3 = set1.union(set2)
print(set3)
print()

# memasukkan dengan update
set4 = {1,2,3}
set5 = {2,4,6}
set4.update(set5)
print(set4)
