'''
Archivo principal, 

'''
import argparse

class Restaurante:
    """
    Representa el concepto del restaurante

    Atributos:  
    servicio (Servicio): Permite manipular a los meseros de una forma sencilla   
    cocina (Cocina): Permite manipular a los cocineros de una forma sencilla  
    clientes (Clientes): Permite manipular a los clientes de una forma sencila  
    """
    pass

    def main(self):
        parser = argparse.ArgumentParser(description="""Este programa permite simular el comportamiento de un\
            de un restaurante. Y los distintos comportamientos concurrentes que estos presentan. 

            Ejemplo de uso:
            python3 restaurante.py 6 3 2 2
            """)
        parser.add_argument("clientes",type=int,help="Numero de clientes")
        parser.add_argument("grupos",type=int,help="Numero de grupos de clientes")
        parser.add_argument("meseros",type=int,help="Numero de meseros")
        parser.add_argument("chefs",type=int,help="Numero de chefs")
        parser.parse_args()
        print(parser.clientes)
        print(parser.grupos)
        print(parser.meseros)
        print(parser.chefs)

if __name__ == "__main__":
    restarurantito = Restaurante()
    restarurantito.main()