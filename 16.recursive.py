def suma(n):
    if n == 0:
        return 0
    else: 
        return n + suma(n - 1)

print(suma(5))

def potencia(a,b):
    if b == 0:
        return 1
    else:
        return a * potencia(a, b-1)
    
print(potencia(2,5))

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
print(fibonacci(6))