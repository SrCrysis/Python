temperatura = float(input("Ingresa la temperatura:"))
escala = input("Es Fahrenheit(F) o es Celsius (C)?:").lower()

if escala == "f":
    celsius = (temperatura - 32) * 5/9
    print(celsius)
elif escala =="c":
    fahrenheit = temperatura * 1.8 + 32
    print(fahrenheit)
else:
    print("La escala ingresada no es correcta.")