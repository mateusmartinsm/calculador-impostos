from descontos import *

class Calculador_de_descontos:
    def calcula(self, orcamento):
        desconto = Desconto_por_cinco_itens(
            Desconto_por_mais_de_quinhentos_reais(
                Sem_desconto()
            )
        ).calcula(orcamento)
        
        return desconto

if __name__ == '__main__':

    from orcamento import *

    orcamento = Orcamento()
    orcamento.adiciona_item(Item('ITEM - 1', 100))
    orcamento.adiciona_item(Item('ITEM - 2', 50))
    orcamento.adiciona_item(Item('ITEM - 3', 400))

    calculador = Calculador_de_descontos()

    desconto = calculador.calcula(orcamento)

    print(f'Desconto calculado R${desconto:.2f}')