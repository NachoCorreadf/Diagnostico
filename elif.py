numero = int(input("Ingresa un numero del 1 al 7: "))

if numero == 1:
  dia = "lunes"

elif numero == 2:
  dia = "martes"

elif numero == 3:
  dia = "miercoles"

elif numero == 4:
  dia = "jueves"

elif numero == 5:
  dia = "viernes"

elif numero == 6:
  dia = "sabado"

elif numero == 7:
  dia = "domingo"

else:
  dia = "Numero invalido"

print("El dia correspondiente al numero ingresado es: ", dia)
