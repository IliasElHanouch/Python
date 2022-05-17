#***Coding in UTF-8***#
"""
@author: Ilias El Hanouch - UC3M
@since: 2022
@PyVersion: 3.9
"""
class Circulo:
    def __init__(self,radio:float):
        self.radio = radio
        #Asumimos que Pi es un atributo inherente a cualquier objeto de la clase círculo
        self.pi = 3.1415926536 #Podría importar la librería math y ahorrarme el declarar el atributo
    """Uso propiedades y setters para garantizar que el radio sea un atributo privado, y que se introducen valores correctos"""
    @property
    def radio(self)->float:
        return self.__radio
    @radio.setter
    def radio(self,radio:float)->float:
        if type(radio) != float:
            raise TypeError("Error. El radio debe de ser un float!!")
        elif radio < 0:
            raise ValueError("Error. Debes introducir un valor de radio mayor que 0")
        else:
            self.__radio = radio
    #Seguimos criterios matemáticos lógicos para calcular el área
    def calcularArea(self):
        """
        Tomamos en cuenta que Área(círculo) = Pi * (Radio)^2
        """
        area = self.pi * (self.__radio**2)
        #Queda algo ad-hoc devolver un texto final, pero ayuda a depurar la cantidad de texto del programa
        txt = ("tiene de área " + str(area) + " unidades al cuadrado")
        return txt
    #Devolevemos la longitud de este
    def calcularLongitud(self):
        """
        Tomamos en cuenta que Longitud(círculo) = 2 * Pi * Radio
        """
        longitud = 2 * self.pi * self.__radio
        #Queda algo ad-hoc devolver un texto final, pero ayuda a depurar la cantidad de texto del programa
        txt = ("tiene de longitud " + str(longitud) + " unidades")
        return txt
    def calcularArco(self):
        ... #*************Pendiente de terminar************************#
    #Método mágico que me devuelve si 2 círculos son idénticos o no, estableciendo como criterio que tengan el mismo radio
    def __eq__(self,other):
        return self.radio == other.radio
    #Devuelvo finalmente un str final, aunque el texto realmente es opcional (queda algo ad-hoc pero depura la cantidad de texto)
    def __str__(self):
        txt = "Un círculo de radio " + str(self.__radio) + " unidades"
        return txt






