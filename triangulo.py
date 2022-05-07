# -*- coding: UTF-8 -*-
"""
@author: Ilias El Hanouch - UC3M
@since: 2022
@PyVersion: 3.9
"""
class Triangulo:
    """
    Creamos el constructor init con parámetro base y altura
    """
    def __init__(self,base: float,altura:float):
        #Lanzamos excepciones para los valores incorrectos
        if base <= 0:
            raise ValueError("No puede ser negativo ni 0!!")
        #Y para tipos también
        elif type(base) != float:
            raise TypeError("La base es un float!!")
        #Si se cumple todo, obtenemos el atributo de la base
        else:
            self.base = base
        #Lo mismo con la altura
        if altura <= 0:
            raise ValueError("No puede ser negativo ni 0!!")
        elif type(base) != float:
            raise TypeError("La altura es un float!!")
        else:
            self.altura = altura
        #Obtenemos la hipotenusa con las respectivos cálculos matemáticos de un Triángulo rectángulo
        self.hipotenusa = (self.base **2 + self.altura **2) **0.5
    #Método para calcular el área
    def calcularArea(self)->float:
        area = (self.altura * self.base) / 2
        #Devolvemos un string con toda la info. Si bien es cierto que hace quedar
        #método "muy ad-hoc", ganamos por su parte ahorrar escritura más tarde
        txt = "tiene de área " + str(area) +" unidades al cuadrado"
        return txt
    #Lo mismo para el perímetro
    def calcularPerimetro(self)->float:
        perimetro = self.hipotenusa + self.base + self.altura
        txt = "tiene de perímetro " + str(perimetro) +" unidades"
        return txt
    #Finalmente el método mágico del str para devolver la cadena de string con toda la info. del triángulo
    def __str__(self) -> str:
        txt = "Un triángulo de base " + str(self.base) + " y altura " + str(self.altura)
        return txt

