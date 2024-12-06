from animal import Animal

class Cachorro(Animal):
    def __init__(self, nome, idade, porte):
        super().__init__(nome, idade)
        self.__porte=porte

    def setPorte(self, porte):
        self.__porte=porte

    def getPorte(self):
        return self.__porte

    def mostrar(self):
        return f"Nome do cachorro: {self.getNome()} \nIdade: {self.getIdade()} \nPorte: {self.getPorte()}"
    
#c = Cachorro("Nina", 5, "Pequeno")
#print(c.mostrar())