x = 2
y = 232

# Condicionales simples
if x > 5:
    print("Es mayor que 5")
elif x == 5:
    print("Es igual a 5")
else:
    print("Es menor que 5")

# Multicondicional
if x > 10 and y < 5:
    print("X es mayor que 10 y Y es mayor que 5")

if x > 10 or y > 25:
    print("X es mayor que 10 o Y es mayor que 25")

if not x>10 :
    print("X no es mayor que 10")

is_member = True
age = 6

if is_member:
    if age>=15:
        print("Tienes acceso porque eres miembro y tienes mas de 15 años")
    else: 
        print("No tienes acceso porque eres miembro pero eres menor de 15 años")
else:
    print("No eres miembro y NO TIENES ACCESO")