a = [1,2,3,4,5]
b = a
print(a)
print(b)
del a[0]
c = a[:] # Metodo Slice para hacer una copia sin modificar la original
print(id(a))
print(id(b))
print(id(c))
a.append(6) # Los cambios se haran tanto en a y b, pero no en c.
print(a)
print(b)
print(c)