class Calculador_de_impostos:
    def realiza_calculo(self, orcamento, imposto):
        if imposto == 'ISS':
            imposto_calculado = orcamento.valor * 0.1
        if imposto == 'ICMS':
            imposto_calculado = orcamento.valor * 0.06
        print(f'R${imposto_calculado:.2f}')

if __name__ == '__main__':
    
    from orcamento import Orcamento

    calculador = Calculador_de_impostos()
    orcamento = Orcamento(500)

    calculador.realiza_calculo(orcamento, 'ISS')
    calculador.realiza_calculo(orcamento, 'ICMS')