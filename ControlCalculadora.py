from Calculadora import Calculadora

class ControlCalculadora:
    def __init__(self):
        self.calcula = Calculadora()
        self.opcao = -1

    def menu(self):
            print("Escolha uma das opções abaixo: \n\n " +
                  "0 .Sair \n" +
                  "1.Somar \n" +
                  "2.Subtrair \n" +
                  "3.Multiplicar\n" +
                  "4.Dividir")
            self.opcao = int(input())

    def operacao(self):
        while (self.opcao != 0):

            self.menu()
            if self.opcao == 0:
                print("obrigado!")

            elif self.opcao == 1:
                print("primeiro numero: ")
                numero1 = int(input())
                print("Segundo numero: ")
                numero2 = int(input())
                self.calcula.somar(numero1, numero2)

            elif self.opcao == 2:
                print("primeiro numero: ")
                numero1 = int(input())
                print("Segundo numero: ")
                numero2 = int(input())
                self.calcula.subtrair(numero1, numero2)

            elif self.opcao == 3:
                print("primeiro numero: ")
                numero1 = int(input())
                print("Segundo numero: ")
                numero2 = int(input())
                self.calcula.multiplicar(numero1, numero2)

            elif self.opcao == 4:
                print("primeiro numero: ")
                numero1 = int(input())
                print("Segundo numero: ")
                numero2 = int(input())
                self.calcula.dividir(numero1, numero2)

            else:
                print("Opção invalida!")