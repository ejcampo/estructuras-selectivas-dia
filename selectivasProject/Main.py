# Simple
a = 33
b = 200

if b > a:
    print(b, "es mayor que", a)

# Double
y = 200
z = 333
if y > z:
    print(y, "es mayor que", z)
else:
    print(y, "no es mayor que", z)

#Multiple
t = 200
p = 207
if a > b:
    print(t, "es mayor que", p)
elif t < p:
    print(t, "es menor que", p)
else:
    print(t, "es igual que", p)

#Enlazadas
x = 10

if x > 10:
    print("por encima de 10,")
    if x > 20:
        print("y tambien por encima de 20!")
    else:
        print("pero no por encima de 20.")

#End y sep
print("estudiar los sabados", end=' ')
print("es igual")

#print("Estudiar los sabados")'
#print("es genial")

#--------------------------------
print("Daniela", "Luis", "Carlos", "Camila") #agrega un espacio por defecto
print("Daniela","Luis","Carlos","Camila", sep="") #Quita espacios
print("Daniela","Luis","Carlos","Camila", sep=",")#Agrega coma

print("Daniela", "Luis", "Carlos", "Camila", sep="_", end="_curso_python")#Implementacion end y sep
print("-----------------------------------------------")
print("")


