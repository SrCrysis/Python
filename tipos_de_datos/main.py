name = "matias"
print (name)
age = '22'
print (age)

total = int(age) + 10
template = f"Hola mi nombre es {name}, tengo {age} anios y en 10 anios tendre {total} anios"
print (template)

number = '7'
print (number)

if int(number) % 2 == 0:
    print('Es par')
else:
    print('Es impar')

    letters = ['A', 'B', 'C', 'D', 'E', 'F']

    letters.append ('G')
    letters[0] = 'Z'
    letters.remove ('C')
    letters.reverse()
    print(letters)

    person = {
        'name': 'Nicolas',
        'lastName': 'Molina',
        'age': 29
    }

    person ['twitter'] = '@nicobytes'
    person ['name'] = 'Felipe'
    del person ['age']

    print(list(person.keys()))
    print(list(person.values()))


texto = "Hola Mundo"
print (texto.upper())
print (texto.lower())
print (texto.find("M"))

