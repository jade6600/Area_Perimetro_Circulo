import math

print ("####################")
print ("area perimetro circulo")
print ("###################")


# input
r=input("digite el valor de radio : ")
r = int(r)

# processing
p=2*math.pi*r
a=math.pi*r*r

# output
print("..........................")
print("el area es: "+ str(a))
print("el perimetro es: " + str(p))
print(".............................")
