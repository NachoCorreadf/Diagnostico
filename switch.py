numero = int(input("Ingrese un numero del 1 al 7: "))

nombre_dia = ""
switch = {
  1: "lunes",
  2: "martes",
  3: "miercoles",
  4: "jueves",
  5:"viernes",
  6: "sabado",
  7: "domingo"
}
nombre_dia = switch.get(numero, "Numero invalido")

print("El dia correspondiente al numero ingresado es: ", nombre_dia)
