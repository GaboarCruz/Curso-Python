mensaje = "Can`t Stop Printing.  "
texto = "EsTe TeXtO eStá cOn LaS létRaS rArAs"
mensaje_tabulado = "tab\ttab\ttab"
nombre = "Luis"
apellido = "Rivera"
numeros = "221"
valoresEspeciales = "@_#"

#print (mensaje[0], mensaje[1], mensaje[2]) # Indice de cadenas.
#print((mensaje + " ") * 3) # Repeticion de cadena.
#print(len(mensaje)); # Tamaño de cadena.
#print(mensaje.lower()) # Metodo para convertir una cadena a minuscula.
#print(mensaje.upper()) # Metodo para convertir una cadena a mayuscula.
#print(mensaje.strip()) # Metodo para quitar los espacios al inicio y final de la cadena.
#print(texto.capitalize()) # Metodo para capitalizar el texto.
#print(texto.casefold()) # Metodo para regresar el texto en minusculas y normalizado.
#print(texto.center(20)) # Metodo para regresar el texto con ciertos espacios antes de que empieze
#print(texto.count("te")) # Metodo para contar cuantas veces se repite una cadena de texto dentro de otra
#print(texto.encode()) # Metodo que regresa el texto como si fuera texto encodificado
#print(texto.endswith("s")) # Metodo que regresa un booleano dependiendo de si la el valor que se pone es el que termina la cadena.
#print(texto.find("Te")); # Metodo que encuentra el indice de donde empieza la cadena especificada.
#print(mensaje_tabulado.expandtabs(1)) # Metodo que modifica el tamaño de los tabuladores
#print("Mi nombre es {0} {1}".format(nombre,apellido)) # Metodo que formatea un texto para usar valores especificos a los que se le asigna un indice para apuntar al valor
#print(nombre.index("luis")) # Metodo que busca el indice donde empieza y si no lo encuentra regresa el ValueError
#print(numeros.isalnum()) # Metodo que regresa un booleano dependiendo de si la cadena solo tiene valores alfanumericos
#print(numeros.isalpha()) # Metodo que regresa un booleano dependiendo de si la cadena es solo tiene letras
#print(valoresEspeciales.isascii()) # Metodo que regresa booleano dependiendo de si la cadena solo tiene valores ascii
#print(numeros.isdecimal()) # Metodo que regresa si la cadena es un numero decimal
#print(numeros.isdigit()) # Metodo que regresa si la cadena solo tiene digitos
print(numeros.join("rs"))