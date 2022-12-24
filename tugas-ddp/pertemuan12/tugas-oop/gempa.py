class Gempa:
    #member1 variabel
    location = ''
    scale = 0
    skala_ritcher = scale

    #member2 konstruktor
    def __init__(check, location, scale):
        check.location = location
        check.scale = scale
        if check.scale <=2 :
            print("Dampaknya: tidak terasa.")
        elif check.scale <= 4 and check.scale >= 2 :
            print("Dampaknya: bangunan retak-retak.")
        elif check.scale <= 6 and check.scale >= 4 :
            print("Dampaknya: bangunan roboh.")
        else :
            print("Dampaknya: bangunan roboh dan berpotensi tsunami.")

    def hasil(check) :
        print("Lokasi gempa: ",check.location)
        print("Besar skala: ",check.scale,"ritcher")