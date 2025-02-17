cosas_que_hacer = ["Ir al dentista",
                   "Ir a almorzar",
                   "Visitar un museo",
                   "Volver al hotel"]
# print(cosas_que_hacer)

numeros = [1,2,3,4,"Cinco"]
# print(numeros)
# print(type(numeros))

mix = ["Cadena", 0, 1, True, False, 0.5, 0.21,  [1,2,3, "one", False, 0.21, 1]]
# print(mix)
# print(len(mix))
# print("Primer elemento:", mix[0])
# print("Tercer elemento:", mix[2])
# print("Ultimo elemento:", mix[-1])

string = "Hola Mundo"
# print("Primer elemento:", string[0])
# print("Tercer elemento:", string[2])
# print("Ultimo elemento:", string[-1])

mix.append(False)
mix.append(["ab", "aa", "ac"])
mix.insert(1, ["ab", "aa", "ac"]) 
print(mix);
print(mix.index(["ab", "aa", "ac"]))

numeros = [1,2,100,3,90.21,4,5]
print(numeros)
print("Mayor:",max(numeros))
print("Menor:",min(numeros))
del numeros[-1]
print(numeros)
del numeros[:2]
print(numeros)
del numeros
print(numeros)