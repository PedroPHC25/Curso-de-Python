# -*- coding: utf-8 -*-

# print('Olá, mundo!')
# print('Outra mensagem')
# print('Mensagem 3')

### Comentário
'''
Comentário
de múltiplas
linhas
'''

### Operações matemáticas
'''
print(2+2)
print(2**3)
print(10%3)
'''

### Variáveis
'''
minha_variavel = "Olá mundo!"
print(minha_variavel)
var1 = 1 # int
var2 = 1.1 # float
var3 = "Texto" # string
var4 = True # bool
print(var1)
print(var2)
print(var3)
print(var4)
'''

### Operadores

x = 3
y = 10
z = 4
'''
soma = x + y
print(x == y)
print(x == y and x == z)
print(x == y or x == z)
'''

### Comandos condicionais
'''
if x > y:
    print('x é maior')

if y > x:
    print('y é maior')

if x == y:
    print('Iguais')
elif x < y:
    print('Menor')
elif y > x:
    print('Maior')
else:
    print('Diferentes')
'''

### Laços
'''
x = 1
while x < 10:
    print(x)
    x += 1


lista = [1, 2, 3, 4, 5]
lista2 = ['a', 'b', 'c', 'd', 'e']
lista3 = [0, 'olá', 'biscoito', 5, 9.99, True]

for i in lista:
    print(i)


for i in range(10, 20, 2):
    print(i)
'''

### Strings
'''
a = 'Pedro '
b = 'Henrique'

print(a + b)

print(len(a + b))

print(a[2])

print(b[0:3])

print(a.lower()) # Torna tudo minúsculo
print(a.upper()) # Torna tudo maiúsculo
print(a.strip()) # Elimina espaços no início e no final da string

ms = 'O rato roeu a roupa do rei de Roma'

print(ms.split('r')) # Divide a string em elementos de uma lista

print(ms.find('rei')) # Encontra um termo na string e retorna seu índice
print(ms[ms.find('rei'):])

print(ms.replace('o rei', 'a rainha')) # Substitui um termo por outro
'''

### Funções
'''
def soma(x, y):
    return x+y

def mult(x, y):
    return x*y

print(soma(9, 5))
print(mult(2, 9))

print(soma(soma(5,9), mult(9, 8)))
'''

### Arquivos
'''
arquivo = open('arquivo') # Armazena um arquivo em uma variável

linhas = arquivo.readlines() # Armazena o TEXTO de um arquivo em uma variável em formato de LISTA

for linha in linhas:
    print(linha)

texto_completo = arquivo.read() # Armazena o TEXTO de um arquivo em uma variável em uma ÚNICA string

print(texto_completo)

w = open('arquivo2', 'w') # Pode abrir um arquivo já existente ou criar um novo se ele não existir

w.write('Esse eh o meu arquivo') # Sobrescreve o conteúdo do arquivo por causa do método 'w'

w.close() # Fecha o arquivo

w2 = open('arquivo', 'a') # Modo 'a': adiciona o texto em vez de sobrescrever

w2.write('\nInserção')

w2.close()
'''

### Listas
'''
lista = ['abacaxi', 'melancia', 'abacate']
lista2 = [1, 2, 3, 4, 5]
lista3 = ['abacaxi', 2, 9.85, True]

print(lista)
print(lista2)
print(lista3)

print(lista[2])

for item in lista:
    print(item)

print(len(lista))

lista.append('limão')

print(lista)

if 3 in lista2:
    print('Sim')

del lista[2:] # Remove elementos de uma lista

print(lista)

del lista2[:] # Remove todos os elementos de uma lista

print(lista2)

lista4 = []

lista4.append(57)

print(lista4)

lista = [1235, 456, 1564, 948488, 2, 0]
lista2 = [1235, 456, 1564, 948488, 2, 0]
lista3 = [1235, 456, 1564, 948488, 2, 0]

lista.sort() # Ordena os elementos de uma lista alterando a lista original

print(lista)

print(sorted(lista)) # Apenas devolve a lista ordenada, sem alterar a original

lista2.sort(reverse = True) # Ordena ao contrário

print(lista2)

lista3.reverse() # Inverte a ordem dos elementos da lista

print(lista3)

lista4 = ['bola', 'abacate', 'dinheiro']

lista4.sort()

print(lista4)

lista4.sort(reverse = True)

print(lista4)
'''

### Dicionários
'''
dic = {'A': 'Ameixa', 'B':'Bola', 'C':'Cachorro'}

print(dic['A'])

print(dic)

for chave in dic: # Sem nenhum método, isso retorna as chaves
    print(chave)

for chave in dic:
    print(chave + ': ' + dic[chave])

for i in dic.items(): # Retorna cada chave e elemento em tuplas
    print(i)

for i in dic.values(): # Retorna os elementos
    print(i)

for i in dic.keys(): # Retorna as chaves
    print(i)
'''

### Números aleatórios
'''
import random # Biblioteca para geração aleatória

x = random.randint(0, 10) # Gera um inteiro aleatório

print(x)

lista = [1, 2, 3, 4, 5]

x = random.choice(lista) # Sorteia um elemento de uma lista

print(x)
'''

### Exceções: try/except
# Se o comando do try apresentar algum erro, ele executa o except e continua a execução do programa normalmente em vez de interromper completamente
'''
a = 2
b = 0

try: 
    print(a/b)
except:
    print('Não pode!!!')

print(a)
'''

### Exercícios:

## 1. Faça um programa que receba a idade do usuário e diga se ele é maior ou menor de idade. 

# O input sempre converte a resposta para string!

'''
idade = int(input('Digite sua idade:'))

if idade < 18:
    print('Você ainda é menor de idade')
else:
    print('Você já é maior de idade')
'''

## 2. Faça um programa que receba duas notas digitadas pelo usuário. Se a nota for maior ou igual a seis, escreva aprovado, senão escreva reprovado.

'''
nota1 = int(input('Digite sua nota da A1:'))
nota2 = int(input('Digite sua nota da A2:'))

if (nota1 + nota2)/2 < 6:
    print('Sinto muito. Você foi reprovado...')
else:
    print('Parabéns! Você foi aprovado!')
'''

## 3. Escreva um programa que resolva uma equação de segundo grau.

'''
import math

a = float(input('Digite o coeficiente a:'))
b = float(input('Digite o coeficiente b:'))
c = float(input('Digite o coeficiente c:'))

x1 = (-b + math.sqrt(b**2 - 4*a*c))/(2*a)
x2 = (-b - math.sqrt(b**2 - 4*a*c))/(2*a)

print(f'As raízes da sua equação são {x1} e {x2}.')
'''

## 4. Escreva um programa que ordene uma lista numérica com três elementos.

'''
lista = []

lista.append(float(input("Digite o primeiro número:")))
lista.append(float(input("Digite o segundo número:")))
lista.append(float(input("Digite o terceiro número:")))

lista.sort()

print(lista)
'''

## 5. Escreva um programa que receba dois números e um sinal, e faça a operação matemática definida pelo sinal.

'''
x = int(input('Insira o primeiro número: '))
s = input('Insira o sinal da operação: ')
y = int(input('Insira o segundo número: '))

if s == '+':
    print(f'O resultado da sua operação é {x+y}.')
elif s == '-':
    print(f'O resultado da sua operação é {x-y}.')
elif s == '*':
    print(f'O resultado da sua operação é {x*y}.')
elif s == '/':
    print(f'O resultado da sua operação é {x/y}.')
elif s == '**':
    print(f'O resultado da sua operação é {x**y}.')
'''

### List comprehension

'''
x = [1, 2, 3, 4, 5]

y = [i**2 for i in x]

print(y)

z = [i for i in x if i%2 == 1]

print(z)
'''

### Enumerate

'''
lista = ['abacate', 'bola', 'cachorro']

for i in range(len(lista)):
    print(i, lista[i])

for i, nome in enumerate(lista):
    print(i, nome)
'''

### Map
# Recebe 2 argumentos: a função e a lista de valores que se quer aplicar a essa função.

'''
def dobro(x):
    return x*2

valor = [1, 2, 3, 4, 5]

print(list(map(dobro, valor)))
'''

### Reduce

'''
from functools import reduce

def soma(x, y):
    return x+y

lista = [1, 2, 3, 4, 5]

x = reduce(soma, lista)

print(x)
'''

### Zip

'''
lista1 = [1, 2, 3, 4, 5]
lista2 = ['abacate', 'bola', 'cachorro', 'dinheiro', 'elefante']
lista3 = [6, 7, 8, 9, 10]

for i, j, k in zip(lista1, lista2, lista3):
    print(i, j, k)
'''