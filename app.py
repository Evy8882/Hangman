# importação da biblioteca utilizada
import random

# Transforma o arquivo txt com as palavras em um array:
with open('words.txt') as f:
    words = f.readlines()

words = [x.rstrip('\n') for x in words]

# alfabeto
letras = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# Pegaa uma palavra e verifica se ela é valida
def validar_palavra(lista_de_palavras):
    word = random.choice(lista_de_palavras)

    while '-' in word or ' ' in word or "'" in word or len(word) < 4:
        word = random.choice(lista_de_palavras)

    return word.upper()

# Jogo
def forca():
    palavra = validar_palavra(words) # Escolhe uma palavra
    palavra_letras = set(palavra) # Cria uma lista com as letras
    alfabeto = set(letras)
    letras_usadas = set()

    while len(palavra_letras): # O código vai se repetir até a palavra ser completamente descoberta
        print(f'Você já usou as seguintes letras: '+ ''.join(letras_usadas))

        palavra_adivinhada = [letra if letra in letras_usadas else '_' for letra in palavra]
        print('Palavra: ' + ''.join(palavra_adivinhada) + '\n')

        user_input = input('Adivinhe a letra: ').upper()
        if user_input in alfabeto - letras_usadas:  # Se a letra foi valida
            letras_usadas.add(user_input)
            if user_input in palavra_letras:        # Se acertou
                palavra_letras.remove(user_input)
                print('ACERTOU UMA LETRA!!!')
            else:                                   # Se errou
                print('Errou!')

        elif user_input in letras_usadas:
            print('essa letra já foi usada'.upper())

        else:
            print('Digite uma letra válida'.upper())
    print(f'Você ganhou, a palavra era "{palavra}"')
forca()


