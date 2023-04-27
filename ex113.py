'''Exercício Python 113: Reescreva a função
leiaInt() que fizemos no desafio 104, incluindo
agora a possibilidade da digitação de um número
de tipo inválido. Aproveite e crie também uma
função leiaFloat() com a mesma funcionalidade.'''


def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))

        except (ValueError, TypeError):
            print('\033[31mERRO: Por favor, Digite um número inteiro válido.\033[m')
            continue

        except (KeyboardInterrupt):
            print('\n\033[31mUsuário prefiriu não digitar esse número.\033[m')
            return 0

        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))

        except (ValueError, TypeError):
            print('\033[31mERRO: Por favor, Digite um número inteiro válido.\033[m')
            continue

        except (KeyboardInterrupt):
            print('\n\033[31mUsuário prefiriu não digitar esse número.\033[m')
            return 0

        else:
            return n



n1 = leiaInt('Digiete um número Inteiro: ')
n2 = leiaFloat('Digite um número Real: ')

print(f'Você digitou o número inteiro {n1} e o número Real {n2:.1f}')
