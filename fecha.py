#****Coding in UTF-8****#
"""
@author: Ilias El Hanouch - UC3M
@since: 2022
@PyVersion: 3.9
"""
class Fecha:
    """
    Creo el constructor init que crea el objeto. Es uno de los "métodos mágicos" al cual le voy a pasar de parámetros el día, mes
    y año
    """
    def __init__(self,dia,mes,anio):
        #Diccionario como atributo privado; no se puede modificar ni dentro ni fuera de la clase.
        self.__dias_mes = {'enero': 31, 'febrero': 28, 'marzo': 31, 'abril': 30,
        'mayo': 31, 'junio': 30, 'julio': 31, 'agosto': 31,
        'septiembre': 30, 'octubre': 31, 'noviembre':30,
        'diciembre': 31}
        #Atributos del init inicialmente sin comprobar ni nada
        self.anio = anio
        self.mes = mes
        self.dia = dia
    """
    Properties y setters por orden de aparición de atributo. Nótese que año, mes y día están dispuestos de forma que
    haya dependencia progresiva
    """
    #Properties y setters de año
    @property
    def anio(self) -> int:
        return self.__anio
    @anio.setter
    def anio(self,anio: int):
        if type(anio) != int:
            raise TypeError("Error. El año es un int!!!")
        elif anio < 0:
            raise ValueError("Error. No puede haber un año negativo!!")
        else:
            self.__anio = anio
    #Bisiesto es sólo de lectura, luego sólo creo su propiedad y no necesito setters
    @property
    def bisiesto(self) -> bool:
        return (self.anio % 4 == 0 and (self.anio % 100 != 0 or
        self.anio % 400 == 0))
    #Properties y setters de mes
    @property
    def mes(self) -> str:
        return self.__mes
    @mes.setter
    def mes(self,mes:str):
        if type(mes) != str:
            raise TypeError("Error. Mes es un string!!")
        elif mes in self.__dias_mes:
            self.__mes = mes
        else:
            raise ValueError("Error, los meses de un año son: ",tuple(self.__dias_mes.keys()))
    #Properties y setters de día
    @property
    def dia(self)-> int:
        return self.__dia
    @dia.setter
    def dia(self,dia)-> int:
        #Condición inicial: si el año es bisiesto, la clave febrero tiene de valor 29 días en lugar de 29
        if self.bisiesto:
            self.__dias_mes["febrero"] = 29
        #Lanzamos excepciones de año
        if type(dia) != int:
            raise TypeError("Error. Día es un entero!!")
        elif dia > 0 and dia <= self.__dias_mes[self.__mes]:
            self.__dia = dia
        else:
            #Queda algo ad-hoc pero depuramos el texto del código
            text = "Error. El día solo puede estar comprendido entre el 0 y el " + str(self.__dias_mes[self.__mes])
            raise ValueError(text)
    def __eq__(self,other):
        """
        Establecemos el criterio para los cuales dos fechas (2 objetos) iguales, lo son también para el programa:
        si coincide el día, mes y año
        """
        return (self.__dia == other.__dia and self.__mes == other.__mes and self.__anio==other.__anio)
    #Método str que me devuelve la fecha completa, y me dice si es bisiesto o no. Todo en una cadena de texto
    def __str__(self) ->str:
        txt = "El " + str(self.__dia) + " de " + str(self.__mes) + " del " + str(self.__anio)
        if self.bisiesto:
            txt+= ". Es un año bisiesto"
        else:
            txt += ". No es un año bisiesto"
        return txt


