#ini class
class Person:
    def __init__(self, name, age, gender, address, hobby):
        self.name = name
        self.age = age
        self.gender = gender
        self.address = address
        self.hobby = hobby
    
    def biodata(self):
        print("Nama saya ", self.name, "Saya seorang ", self.gender, "Saya tinggal di ", self.address, "Hobi saya adalah ", self.hobby)
    
#ini objek 
orang1 = Person("Angga", 30, "Laki-laki", "Depok", "Hiking")
orang2 = Person("Naya", 20, "Perempuan", "Jakarta", "Cooking")

orang1.biodata()
orang2.biodata()

# orang1.name = "Kayla"
# orang1.gender = "Perempuan"

# print(orang1.name)
# print(orang1.age)
# print(orang1.gender)
# print(orang1.address)
# print(orang1.hobby)


