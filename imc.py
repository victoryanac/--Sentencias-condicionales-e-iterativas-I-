#ingreso de datos usuario
peso =  float(input("Ingrese peso en kg: "))
talla_cm = float(input("Ingrese talla en cm: "))

#convertidor de cm a mts
talla_mts = talla_cm/100

#calculo de IMC
imc = peso / talla_mts ** 2

print(f"Su IMC es {imc: .2f} kg/mts2")

#clasificaion de IMC adulto
if imc < 18.5:
    print("La clasificación OMS es Bajo Peso")
elif 18.5 <= imc < 25:
    print("La clasificación OMS es Adecuado")
elif 25 <= imc < 30:
    print("La clasificación OMS es Sobrepeso")
elif 30 <= imc < 35:
    print("La clasificación OMS es Obesidad Grado I")
elif 35 <= imc < 40:
    print("La clasificación OMS es Obesidad Grado II")
elif imc >= 40:
    print("La clasificación OMS es Obesidad Grado III")