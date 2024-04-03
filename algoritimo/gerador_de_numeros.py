
#bibliteca para gerar números aleatórios e outras operações relacionadas a aleatoriedade
import random
#Nome do Programa
print('fazendo test')
print("*"*8+"Meu gerador de números da sorte"+"*"*8)
#variavel com função input solicitando a data do dia atual
data_nascimento = input("Insira a data de hoje o para gerar seus números da sorte \n(formato: YYYY/MM/DD): ")

#Esse código lê a data de nascimento, usa os valores para semente da função de geração de números aleatórios e imprime 12 números aleatórios entre 1 e 80.
#A função map() aplica uma função a todos os itens de um iterável e retorna um iterador com os resultados. Neste caso, a função int() está sendo aplicada a cada substring resultante do método split().
ano, mes, dia = map(int,  data_nascimento.split('/'))
random.seed((ano, mes, dia))
#Esse código gera e imprime 12 números inteiros aleatórios entre 1 e 80.
for _ in range(12):
    print(random.randint(1, 80))

#bibliteca para gerar números aleatórios e outras operações relacionadas a aleatoriedade
import random
#Nome do Programa
print("*"*8+"Meu gerador de números da sorte"+"*"*8)
#variavel com função input solicitando a data do dia atual
data_nascimento = input("Insira a data de hoje o para gerar seus números da sorte \n(formato: YYYY/MM/DD): ")

#Esse código lê a data de nascimento, usa os valores para semente da função de geração de números aleatórios e imprime 12 números aleatórios entre 1 e 80.
#A função map() aplica uma função a todos os itens de um iterável e retorna um iterador com os resultados. Neste caso, a função int() está sendo aplicada a cada substring resultante do método split().
ano, mes, dia = map(int,  data_nascimento.split('/'))
random.seed((ano, mes, dia))
#Esse código gera e imprime 12 números inteiros aleatórios entre 1 e 80.
for _ in range(12):
    print(random.randint(1, 80))

