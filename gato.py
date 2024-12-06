from animal import Animal

class Gato(Animal):
    def __init__(self, nome, idade, raca):
        super().__init__(nome, idade)
        self.__raca=raca

    def setRaca(self, raca):
        self.__raca=raca

    def getRaca(self):
        return self.__raca
    
    def mostrar(self):
        return f"Nome do gato: {self.getNome()}\n Idade: {self.getIdade()}\n Raça: {self.getRaca()}"
    
#g=Gato("Félix", 2, "Anúbis")
#print(g.mostrar())
