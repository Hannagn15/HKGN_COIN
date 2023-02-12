def saludar():
    print("hola desde ",__name__)


#se utiliza para asegurar de que alguna funcion
#se ejecute solo dentro del mismo modulo
if __name__ == "__main__":
    saludar()
else:
    print("no se ejecuta fuera del modulo")    