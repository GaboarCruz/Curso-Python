numbers = {
    1: "uno",
    2: "dos",
    3: "tres"
}
# print(numbers[3])
information = {
    "name": "Luis",
    "apellido": "Guerra",
    "altura": "1.75",
    "edad": 21
}
# print(information)
# del information["edad"]
# print(information)

claves = information.keys()
# print(claves)
# print(type(claves))
values = information.values()
# print(values)
# print(type(values))
pairs = information.items()
# print(pairs)
# print(type(pairs))

contacts = {
    "Luis":{"apellido": "Guerra",
    "altura": 1.75,
    "edad": 21},

    "Carlos":{"apellido": "Ramírez",
    "altura": 1.80,
    "edad": 25},

    "Andrea":{"apellido": "Fernández",
    "altura": 1.65,
    "edad": 30},

    "Mariana":{"apellido": "López",
    "altura": "1.70",
    "edad": 28},

    "Javier": {"apellido": "Torres",
    "altura": "1.78",
    "edad": 22}
}

print(contacts["Luis"])