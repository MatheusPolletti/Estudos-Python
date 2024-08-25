# arquivo = open('nomedoarquivo', 'função')

# É possível combinações
# r - leitura
# w - escrita
# a - acrescentar
# x - cria novo arquivo, se não existir
# b - arquivo binário
# t - modo de texto

# arquivo.read() - Ler
# arquivo.readline() - Ler uma linha
# arquivo.readlines() - Ler por linha, lista

# arquivo.write('texto') - arquivo.close()

#with open('nomedoarquivo', 'função) as arquivo:
#   conteudo = arquivo.read()
#   print(conteudo)

"""arquivo = open('provas.txt', 'w')

arquivo.write('Eu quero testar umas coisas\nVou escrever aqui e ver o que dá\nBora lá')
arquivo.close()"""

"""arquivo = open('provas.txt', 'a')

arquivo.write('Aumentando as coisas escritas\nQue maneiro ein')
arquivo.close()"""

"""with open('provas.txt', 'r') as arquivo:
    print(arquivo.readlines())"""

"""open('teste.txt', 'w')

with open('test.txt', 'a+') as arquivo:
    arquivo.write('Testes fodas\nMuito foda mesmo')"""

"""imagem = open('te', 't+x')

imagem.write('teste')"""
