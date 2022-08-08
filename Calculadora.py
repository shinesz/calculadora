class Calculadora:
    def __init__ (self):
        self.numero1 = ""
        self.numero2 = ""

    #metodo de acesso

    def getNumero1(self):
        return self.numero1

    def getNumero2(self):
        return self.numero2

    def setNumero1(self, numero1):
        self.numero1 = numero1

    def setNumero2(self, numero2):
        self.numero2 = numero2

    #somar

    def somar(self, numero1, numero2):
        print(numero1 + numero2)


    #subtrair

    def subtrair(self, numero1, numero2):
        print(numero1 - numero2)

    #multiplicar

    def multiplicar(self, numero1, numero2):
            print(numero1*numero2)

    #dividir

    def dividir(self, numero1, numero2):
        print(numero1 // numero2)