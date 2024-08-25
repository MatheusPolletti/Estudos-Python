class Vendedor():
    def __init__(self, nome_vendedor) -> None:
        self.nome_vendedor = nome_vendedor
        self.vendas = 0

    def vendeu(self, vendas) -> None:
        self.vendas = vendas

    def bateu_meta(self, meta) -> str:
        if self.vendas > meta:
            print(f'O vendedor {self.nome_vendedor} bateu a meta de venda de R${meta}.')
        else:
            print(f'O vendedor {self.nome_vendedor} não bateu a meta de vendas.')
    
    def dia_trabalho(self, dia_semana) -> str:
        dia_semana = dia_semana.lower().strip().replace('á', 'a')
        if dia_semana == 'domingo':
            print(f'O vendedor {self.nome_vendedor} não trabalha nesse dia.')
        elif dia_semana == 'sabado':
            print(f'O vendedor {self.nome_vendedor} só trabalha meio período nesse dia.')
        else:
            print(f'O vendedor {self.nome_vendedor} trabalha normalmente nesse dia.')

vendedor_01 = Vendedor('Matheus')

vendedor_01.vendeu(1000)

vendedor_01.bateu_meta(500)

vendedor_01.dia_trabalho('domingo')
vendedor_01.dia_trabalho('Sábado')
vendedor_01.dia_trabalho('segunda      ')