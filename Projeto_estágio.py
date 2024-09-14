# Desafio 1
"""
limite = int(input(
    'Informe quantos valores da Sequência de Fibonacci você quer que seja desenvolvido: '))
procurado = int(input(
    f'Informe qual valor você quer procurar na sua Sequência de Fibonacci de {limite} digitos: '))
fibo = 0
n1 = n3 = 0
n2 = 1
encontrado = False
while fibo < limite:
    print(n3)

    if n3 == procurado:
        encontrado = True
        break
    n1 = n2
    n2 = n3
    n3 = n1 + n2
    fibo += 1

if encontrado:
    print(f'O número {procurado} foi encontrado na sequência!')
else:
    print(f'O número {procurado} não foi encontrado!')

#Desafio 2
palavra = str(input('Informe uma palavra: '))

A = palavra.count('A')
a = palavra.count('a')
Tot = A+a
if Tot > 0:
    print(f' A letra "a" apareceu {a} vezes, e a letra "A" apareceu {A} vezes, no total, elas aparecerem {Tot} vezes')
else:
    print('A letra "a" e "A" não foram encontradas')

# Desafio 3
Indice = 12
Soma = 0
K = 1
while K < Indice:
    K = K + 1
    Soma = Soma + K
    print(Soma)
print(f'A variável Soma, ficou com o valor {Soma}')
"""

# Desafio 4
# a) 1, 3, 5, 7, 9(Como 1 não é considerado número primo, não seria valor 11)
# b) 2, 4, 8, 16, 32, 64, 128 (2x2x2x2x2x2x2)
# c) 0, 1, 4, 9, 16, 25, 36, 49(Sequência dos números de quadrados perfeitos; 7² = 49)
# d) 4, 16, 36, 64, 100 (Sequência de quadrados perfeitos com base em números pares(10²= 100))
# e) 1, 1, 2, 3, 5, 8, 13(Sequência de Fibonacci)
# f) 2, 10, 12, 16, 17, 18, 19, 200(Número que começam com a letra D, caiu em uma questão da OBMEP)

# Desafio5
# Um Sistema de calor é o necessário para saber!
# Liga-se um interruptor por um certo tempo, eu faria 10 minutos por garantia, depois desligaria ele e ligaria outro.
# Neste momento eu faria a primeira ida e analisaria as lâmpadas
# 1.Caso estivesse desligada e quente, seria o interruptor 1 ligado à esta sala
# 2.Caso estivesse ligada, seria o interruptor 2 ligado à esta sala
# 3.Caso estivesse desligada e Fria, seria o interruptor 3 ligado à esta sala
# E então, voltaria, desligaria todas as lâmpadas, e uma das lâmpdas das salas que faltaram, e então faria minha segunda ida
# Analisando a sala se ela estiver ligada ou desligada, eu saberia a qual interruptor todas elas pertencem.
