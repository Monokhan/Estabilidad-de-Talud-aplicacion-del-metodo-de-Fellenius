
import math

print("-------------------------------------------")
print("\n Bienvenido a programa talud v.1 ")
""" 
origenx = float(input("ingrese la coordenada x del centro de la falla:"))
origeny = float(input("ingrese la coordenada y del centro de la falla:"))
radio = float(input("ingrese el radio:"))
crestax = float(input("ingrese la coordenada x de la cresta:"))
crestay = float(input("ingrese la coordenada y de la cresta:"))
toex = float(input("ingrese la coordenada x del toe:"))
toey = float(input("ingrese la coordenada y del toe:"))
nDovelas = int(input("ingrese el numero de dovelas:"))
PesoEspecifico = float(input("ingrese el peso especifico (Kgf/m3):"))
Cohesion = float(input("ingrese la cohesion (kgf/m2):"))
AnguloFI = float(input("ingrese el angulo de friccion interna (°):"))
"""
print("-------------------------------------------")

origenx = 1254.69
origeny = 1360.91
radio = 29.78
crestax = 1276.28
crestay = 1356.39
toex = 1246.28
toey = 1336.39
nDovelas = 15
PesoEspecifico = 1842.12
Cohesion = 2538.85
AnguloFI = 20



# Calcular el punto de corte infrior y superior
d1 = origeny - crestay
d2 = origeny - toey

beta1 = math.asin(d1/radio)
beta2 = math.asin(d2/radio)

x1 = origenx + radio * math.cos(beta1)
x2 = origenx - radio * math.cos(beta2)

Ps = [x1, crestay]
Pi = [x2, toey]

# Longitud de la dovela
long_dovela = (Ps[0]- Pi[0])/nDovelas

# Calculamos la pendiente de la recta inclinada
a = (crestay - toey) / (crestax -toex)
b = crestay - a * crestax
 
# Area  / Peso / variacion de L
Lpesos = []
Lareas = []
Lbases = []

for i in range(nDovelas):
    Xi = Ps[0] - (i + 1) * long_dovela
    Xd = Ps[0] - i * long_dovela

        # Poligono............................1
    if Xi > crestax and i  == 0:
        P1 = [Xi, crestay]
        P2 = [Xi, origeny - radio * math.sin(math.acos((Xi-origenx) / radio))]
        P3 = Ps
        A = (P1[0]* P2[1] + P2[0] * P3[1] + P3[0] * P1[1])
        B = (P1[1]* P2[0] + P2[1] * P3[0] + P3[1] * P1[0]) 
        area = 0.5 * (A - B)
        peso = PesoEspecifico * area
        base = math.sqrt((P2[1] - P3[1])** 2 + (P2[0] - P3[0])**2)
        Lareas.append(area)
        Lpesos.append(peso)
        Lbases.append(base)
        print("p1---------------", i)

        # Poligono............................2
    elif Xi < crestax and i == 0:

        P1 = [Xi, a * Xi + b]
        P2 = [Xi, origeny - radio * math.sin(math.acos((Xi-origenx) / radio))]
        P3 = Ps
        P4 = [crestax, crestay]
        A = (P1[0]* P2[1] + P2[0] * P3[1] + P3[0] * P4[1] + P4[0] * P1[1])
        B = (P1[1]* P2[0] + P2[1] * P3[0] + P3[1] * P4[0] + P4[1] * P1[0]) 
        area = 0.5 * (A - B)
        peso = PesoEspecifico * area
        base = math.sqrt((P2[1] - P3[1])** 2 + (P2[0] - P3[0])**2)
        Lareas.append(area)
        Lpesos.append(peso)
        Lbases.append(base)
        print("p2---------------", i)
 
        # Poligono............................3
    elif Xi < crestax < Xd:

        P1 = [Xi, a * Xi + b]
        P2 = [Xi, origeny - radio * math.sin(math.acos((Xi-origenx) / radio))]
        P3 = [Xd, origeny - radio * math.sin(math.acos((Xd-origenx) / radio))]
        P4 = [Xd, crestay]
        P5 = [crestax, crestay]

        A = (P1[0]* P2[1] + P2[0] * P3[1] + P3[0] * P4[1] + P4[0] * P5[1] + P5[0] * P1[1])
        B = (P1[1]* P2[0] + P2[1] * P3[0] + P3[1] * P4[0] + P4[1] * P5[0] + P5[1] * P1[0]) 
        area = 0.5 * (A - B)
        peso = PesoEspecifico * area
        base = math.sqrt((P2[1] - P3[1])** 2 + (P2[0] - P3[0])**2)
        Lareas.append(area)
        Lpesos.append(peso)
        Lbases.append(base)
        print("p3---------------", i)

        # Poligono............................4
    elif Xi > crestax and i != 0:

        P1 = [Xi, crestay]
        P2 = [Xi, origeny - radio * math.sin(math.acos((Xi-origenx) / radio))]
        P3 = [Xd, origeny - radio * math.sin(math.acos((Xd-origenx) / radio))]
        P4 = [Xd, crestay]
        
        A = (P1[0]* P2[1] + P2[0] * P3[1] + P3[0] * P4[1] + P4[0] * P1[1])
        B = (P1[1]* P2[0] + P2[1] * P3[0] + P3[1] * P4[0] + P4[1] * P1[0]) 
        area = 0.5 * (A - B)
        peso = PesoEspecifico * area
        base = math.sqrt((P2[1] - P3[1])** 2 + (P2[0] - P3[0])**2)
        Lareas.append(area)
        Lpesos.append(peso)
        Lbases.append(base)
        print("p4---------------", i)

      # Poligono............................5  
    elif Xi < toex < Xd and i != nDovelas - 1:

        P1 = [Xi, toey]
        P2 = [Xi, origeny - radio * math.sin(math.acos((Xi-origenx) / radio))]
        P3 = [Xd, origeny - radio * math.sin(math.acos((Xd-origenx) / radio))]
        P4 = [Xd, a * Xd + b]
        P5 = [toex, toey]
        
        A = (P1[0]* P2[1] + P2[0] * P3[1] + P3[0] * P4[1] + P4[0] * P5[1] + P5[0] * P1[1])
        B = (P1[1]* P2[0] + P2[1] * P3[0] + P3[1] * P4[0] + P4[1] * P5[0] + P5[1] * P1[0]) 
        area = 0.5 * (A - B)
        peso = PesoEspecifico * area
        base = math.sqrt((P2[1] - P3[1])** 2 + (P2[0] - P3[0])**2)
        Lareas.append(area)
        Lpesos.append(peso)
        Lbases.append(base)
        print("p5---------------", i)   


     # Poligono............................6  
    elif Xd < toex and i != nDovelas - 1:

        P1 = [Xi, toey]
        P2 = [Xi, origeny - radio * math.sin(math.acos((Xi-origenx) / radio))]
        P3 = [Xd, origeny - radio * math.sin(math.acos((Xd-origenx) / radio))]
        P4 = [Xd, toey]
        
        A = (P1[0]* P2[1] + P2[0] * P3[1] + P3[0] * P4[1] + P4[0] * P1[1] )
        B = (P1[1]* P2[0] + P2[1] * P3[0] + P3[1] * P4[0] + P4[1] * P1[0] ) 
        area = 0.5 * (A - B)
        peso = PesoEspecifico * area
        base = math.sqrt((P2[1] - P3[1])** 2 + (P2[0] - P3[0])**2)
        Lareas.append(area)
        Lpesos.append(peso)
        Lbases.append(base)
        print("p6---------------", i)   

      # Poligono............................7  
    elif Xd < toex and i + 1 == nDovelas:

        P1 = Pi
        P2 = [Xd, origeny - radio * math.sin(math.acos((Xd-origenx) / radio))]
        P3 = [Xd, toey]
        
         
        A = (P1[0]* P2[1] + P2[0] * P3[1] + P3[0] * P1[1])
        B = (P1[1]* P2[0] + P2[1] * P3[0] + P3[1] * P1[0]) 
        area = 0.5 * (A - B)
        peso = PesoEspecifico * area
        base = math.sqrt((P2[1] - P3[1])** 2 + (P2[0] - P3[0])**2)
        Lareas.append(area)
        Lpesos.append(peso)
        Lbases.append(base)
        print("p7---------------", i)   


        # Poligono............................8  
    elif Xd > toex and i + 1  == nDovelas:
  
        P1 = Pi
        P2 = [Xd, origeny - radio * math.sin(math.acos((Xd-origenx) / radio))]
        P3 = [Xd, a * Xd + b]
        P4 = [toex, toey]
         
        A = (P1[0]* P2[1] + P2[0] * P3[1] + P3[0] * P4[1] + P4 [0] * P1 [1])
        B = (P1[1]* P2[0] + P2[1] * P3[0] + P3[1] * P4[0] + P4 [1] * P1 [0]) 
        area = 0.5 * (A - B)
        peso = PesoEspecifico * area
        base = math.sqrt((P2[1] - P3[1])** 2 + (P2[0] - P3[0])**2)
        Lareas.append(area)
        Lpesos.append(peso)
        Lbases.append(base)
        print("p8---------------", i)  


     # Poligono............................9  
    elif Xi > toex and Xd < crestax:

        P1 = [Xi, a * Xi + b]
        P2 = [Xi, origeny - radio * math.sin(math.acos((Xi-origenx) / radio))]
        P3 = [Xd, origeny - radio * math.sin(math.acos((Xd-origenx) / radio))]
        P4 = [Xd, a * Xd + b]
         
        A = (P1[0]* P2[1] + P2[0] * P3[1] + P3[0] * P4[1] + P4 [0] * P1 [1])
        B = (P1[1]* P2[0] + P2[1] * P3[0] + P3[1] * P4[0] + P4 [1] * P1 [0]) 
        area = 0.5 * (A - B)
        peso = PesoEspecifico * area
        base = math.sqrt((P2[1] - P3[1])** 2 + (P2[0] - P3[0])**2)
        Lareas.append(area)
        Lpesos.append(peso)
        Lbases.append(base)
        print("p9---------------", i) 

print(Lareas)     

# lista de angulos
Langulos = []
# lista de F normales
LFnormales = []
# lista de esfuerzos normales
LEnormales = []
# lista de fuerzas resistentes
LFresistentes = []
# lista de momentos actuantes
LMactuantes = []
# lista de momentos resistentes
LMresistentes = []

for i in range(nDovelas):
    # calculamos el angulo alfa
    alfa = math.acos((Ps[0] - origenx - (i + 0.5) * long_dovela) / radio)
    teta = (math.pi / 2) - alfa

    # F normal y E normal
    N = Lpesos[i] * math.cos(teta)
    sigma = N / Lbases [i]

    # Esfuerzo tangencial y F tangencial
    t = Cohesion + sigma * math.tan(math.radians(AnguloFI))
    s = t * Lbases[i]

    # Momento F actuantes Momento F resistentes
    MA = Lpesos[i] * math.cos(alfa) * radio
    MR =  s * radio

    LMresistentes.append(MR)
    LMactuantes.append(MA)
# Funsion suma de la lista de los momento resistente / suma lista momento resistente
FS = sum(LMresistentes) / sum(LMactuantes)    

print("==================================================")
print(FS)
print("==================================================")