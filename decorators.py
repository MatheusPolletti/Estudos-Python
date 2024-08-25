import time

def calcula_duracao(funcao):
    def wrapper():
        tempo_inicial = time.time()
        funcao()
        tempo_final = time.time()

        return f'O tempo gasto na execução do código foi de {tempo_final - tempo_inicial}'

    return wrapper

@calcula_duracao
def main():
    for n in range(0, 10000000):
        pass

print(main())
