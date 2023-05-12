# farawcalculate ver 1.0 rev. 1
import time
# Calculadora de Faraw, hecha por el equipo de Faraw.
print("¡Bienvenido a la calculadora de Faraw!")
# si el mensaje se imprime correctamente, significa que se translado a main.py correctamente!
import os
def decos():
    print("¿Necesita hacer otro calculo?")
    reacion = input("user@faraw $ ")
    if str(reacion.capitalize()) in ["Si", "Y", "S"]:
        os.system("clear")
        reop()
    elif str(reacion.capitalize()) in ["No", "N"]:
        print("¿Quiere salir del programa? (S/N)")
        confirmacion = input("user@faraw $ ")
        if confirmacion.lower() == "s":
            os.abort()
        else:
            decos()
def suma():
     print("Elegiste 'suma', para comenzar a sumar decide el primer sumado: ")
     sumado1 = input("user@faraw $ ")
     print("¿Con que lo vas a sumar?")
     sumado2 = input("user@faraw $ ")
      # Define una variable llamada "calculo", esta calcula la suma entre las variables float sumado1 y sumado2.
     try: calculo = float(sumado1) + float(sumado2)
     except ValueError:
         print("Se produjo un problema, por favor informa a Faraw sobre esto en github, para ello ve a la pestaña de issues y crea uno nuevo dando detalles sobre como causar este problema y que te aparece en la consola, https://github.com/fefedevv/FarawCalculate/issues. El registro es el siguiente \n")
         time.sleep(2)
     # Da a el usuario el resultado.
     print(sumado1, "+", sumado2, " es", calculo)
     decos()
def reop():
    print("¿Que operacion necesita hacer? (suma, resta, multiplicacion o division)")
    operacionA = input("user@faraw $ ")
    if operacionA.lower() == "suma":
        suma()
    elif operacionA.lower() == "resta":
        resta()
    elif operacionA.lower() == "multiplicacion":
        multiplicar()
    elif operacionA.lower() == "division":
        None
    else:
        print("No te he podido entender, por favor revisa lo que has escrito.")
        reop()
def resta():
     print("Elegiste 'resta', para comenzar a restar decide el primer minuendo: ")
     restado1 = input("user@faraw $ ")
     print("¿Con que lo vas a restar?")
     restado2 = input("user@faraw $ ")
      # Define una variable llamada "calculo", esta calcula la suma entre las variables float sumado1 y sumado2.
     
     try: calculo = float(restado1) - float(restado2)
     except ValueError:
         print("Se produjo un problema, por favor informa a Faraw sobre esto en github, para ello ve a la pestaña de issues y crea uno nuevo dando detalles sobre como causar este problema y que te aparece en la consola, https://github.com/fefedevv/FarawCalculate/issues. El registro es el siguiente \n")
         time.sleep(2)
      # Da a el usuario el resultado.
     print(restado1, "-", restado2, " es", calculo)
     decos()
def division():
     print("Elegiste 'division', para comenzar a dividir decide el primer dividendo: ")
     div1 = input("user@faraw $ ")
     print("¿Por cuanto lo vas a dividir?")
     div2 = input("user@faraw $ ")
      # Define una variable llamada "calculo", esta calcula la suma entre las variables float sumado1 y sumado2.
     try: calculo = float(div1) / float(div2)
     except ValueError:
         print("Se produjo un problema, por favor informa a Faraw sobre esto en github, para ello ve a la pestaña de issues y crea uno nuevo dando detalles sobre como causar este problema y que te aparece en la consola, https://github.com/fefedevv/FarawCalculate/issues. El registro es el siguiente \n")
         time.sleep(2)
      # Da a el usuario el resultado.
     print(div1, "/", div2, " es", calculo)
     decos()
def multiplicar(): 
     print("Elegiste 'multiplicar', para comenzar a multiplicar decide el primer multiplicando: ")
     mul1 = input("user@faraw $ ")
     print("¿Con que lo vas a multiplicar?")
     mul2 = input("user@faraw $ ")
      # Define una variable llamada "calculo", esta calcula la suma entre las variables float sumado1 y sumado2.
     
     try: calculo = float(mul1) * float(mul2)
     except ValueError:
         print("Se produjo un problema, por favor informa a Faraw sobre esto en github, para ello ve a la pestaña de issues y crea uno nuevo dando detalles sobre como causar este problema y que te aparece en la consola, https://github.com/fefedevv/FarawCalculate/issues. El registro es el siguiente \n")
         time.sleep(2)
      # Da a el usuario el resultado.
     print(mul1, "*", mul2, " es", calculo)
     decos()
print("Para comenzar, elige una operacion basica para hacer:")
print(" SUMA  RESTA  DIVISION  MULTIPLICACION")
operacion = input("user@faraw $ ")
if operacion.lower() == "suma":
    suma()
elif operacion.lower() == "resta":
    resta()
elif operacion.lower() == "multiplicacion":
    multiplicar()
elif operacion.lower() == "division":
    division()
else:
    print("No te he entendido, revisa tu respuesta e intentalo nuevamente.")
    decos()