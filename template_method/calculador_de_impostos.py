from impostos import *

class Calculador_de_impostos:
    def realiza_calculo(self, orcamento, imposto):
        imposto_calculado = imposto.calcula(orcamento)

        print(f'R${imposto_calculado:.2f}')

if __name__ == '__main__':
    
    from orcamento import *

    calculador = Calculador_de_impostos()

    orcamento = Orcamento()
    orcamento.adiciona_item(Item('ITEM - 1', 50))
    orcamento.adiciona_item(Item('ITEM - 2', 200))
    orcamento.adiciona_item(Item('ITEM - 3', 250))

    print('ISS e ICMS')
    calculador.realiza_calculo(orcamento, ISS())
    calculador.realiza_calculo(orcamento, ICMS())

    print('ICPP e IKCV')
    calculador.realiza_calculo(orcamento, ICPP())
    calculador.realiza_calculo(orcamento, IKCV())