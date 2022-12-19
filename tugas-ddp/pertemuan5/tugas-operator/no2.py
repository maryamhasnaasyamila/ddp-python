# membuat program untuk merubah suhu dari fahrenheit ke celcius dan reamur

f = int(input ("Masukan nilai suhu dalam fahrenheit = "))
#fahrenheit ke celcius
msg1 = "Convert Fahrenheit ke Celcius"
print(msg1)
p = 5/9
q = f-32
c = p*q
print(c)

#fahrenheit ke reamur
msg2 = "Convert Fahrenheit ke Reamur"
print(msg2)
a = 4/9
b = f-32
r = a*b
print(r)