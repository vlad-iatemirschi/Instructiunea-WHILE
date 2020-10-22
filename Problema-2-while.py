a=1
b=0
suma1=0
suma2=0
ap=0
an=0
while (a<=12):
    a=a+1
    b=eval(input("dati temperatura"))
    if b>=0:
        suma1+=b
        ap+=1
    elif b<0:
        suma2+=b
        an+=1

print("temperatura medie pozitiva este",suma1/ap,"grade")
print("tempereatura medie negativa este",suma2/an,"grade")
