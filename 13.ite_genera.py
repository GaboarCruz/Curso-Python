lista =[1,2,3,4,5]

iterar = iter(lista)
""""
print(next(iterar))
print(next(iterar))
print(next(iterar))
"""

cadena = "Hola Mundo"
iterar = iter(cadena)

"""
for char in cadena:
    print(char)
"""
      
# Fibonacci
# 0 1 1 2 3 5 8 12....

def fibonacci(limit):
    a,b = 0,1
    while a < limit:
        yield a
        a,b = b, a+b

'''
for num in fibonacci(20):
   print(num) 
'''