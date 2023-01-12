'''
def anobissexto(ano):
    if ano % 400 == 0:
        return "Sim"
    elif ano % 100 == 0:
        return "Nao"
    elif ano % 4 == 0:
        return "Sim"
    else:
        return "Nao"
def soma_harmonica(k):
    x = 0
    while k >= 1:
        if k == 1:
            x += 1
            k -= 1
        else:
            x += (k ** -1)
            k -= 1
    
    return k
print(3 ** -1)
import numpy as np
n = int(input())
def verificaAprovacao(n):
    while n >= 1:
        n1, n2, n3 = input().split()
        aluno = [float(n1), float(n2), float(n3)]
        if sum(aluno) / 3 >= 7:
            print(f'O ALUNO {n} FOI APROVADO')
        else:
            print(f'O ALUNO {n} FOI REPROVADO')'''

'''def verificaAprovacao(x, y, z, n):
    if (x + y + z) / 3 >= 7:
        print(f'O ALUNO {n} FOI APROVADO')
    else:
        print(f'O ALUNO {n} FOI REPROVADO')
alunos = int(input())
i = 0
while i < alunos:
    aluno = input.split()
aluno = np.array
alunos = np.array
for x in range(2):
    for x in range(5):
        aluno.append(x)
    alunos.append(aluno)
print(alunos)
print(aluno)
n = int(input())
alunos = []
for x in range(n):
    n1, n2, n3 = input().split()
    aluno = [float(n1), float(n2), float(n3)]
    alunos.append(aluno)
def verificaAprovacao(n):
    i = 0
    while i < n:
        if sum(alunos[i]) / 3 >= 7:
            print(f'O ALUNO {i} FOI APROVADO')
        else:
            print(f'O ALUNO {i} FOI REPROVADO')
        i += 1
verificaAprovacao(n)
#vai toma no cu
cota = float(input())
tam = int(input())
qnt = int(input())
valor = tam * cota + cota * tam * 0.025
for x in range(qnt):
    print('Lote: - Total da venda: R$ %.2f' % (x + 1, valor))'''

'''senha = input()
print("senha valida." if 6 <= len(senha) <= 32 and 
all(x.isalnum() for x in senha) and any(x.isdigit() for x in senha) and
 any(x.isupper() for x in senha) and any(x.islower() for x in senha) else "senha invalida.")'''
'''print(6 <= len(senha) <= 32)
print(all(x.isalnum() for x in senha))
print(any(x.isdigit() for x in senha))
print(any(x.isupper() for x in senha))
print(any(x.islower() for x in senha))'''

'''variavel = 0
linhas = int(input())
for i in range(linhas):
    instruc = input()
    variavel = variavel + 1 if '++' in instruc else variavel - 1
print(variavel)'''

'''def area(arg1, arg2, forma):
    if forma == 'retangulo':
        print('O {} tem {:.0f} de area'.format(forma, arg1*arg2))
    elif forma == 'triangulo' or forma == 'losango':
        print('O {} tem {:.0f} de area'.format(forma, (arg1*arg2)/2))
    if forma == 'circulo':
        print('O {} tem {:.0f} de area'.format(forma, (3*arg1*arg1)))
area(15, 3, 'circulo')'''

'''def fazString(x):
    frase = ''
    num = 0
    letra = ''
    for i in range(0, len(x)):
        if x[i].isalpha:
            letra = x[i]
            print(letra)
        else:
            num = int(x[i])
            print(num)
            while x[i + 1].isnumeric():
                i += 1
                num = num * 10 + int(num[i])
                print(num)
            print(num)
            print(letra)
            print(letra * num)
            frase += f'{letra * num}'
            print(frase)
    print(frase)
    print(letra * num)
def checaLetra(x):
    if x.isalpha:
        return x
    else:
        
vezes = int(input())
for a in range(0, vezes):
    fazString(input())
'''

#Questão 24

'''a = []
for i in range(4):
    b = int(input())
    if int(input()) not in a: a.append(int(input()))
final = int(input())
numeros = []
if a[0] == 1 and len(set(a)) == 1:
    print(final)
else:
    for x in range(len(a)):
        i = 1
        while i * a[x] <= final:
            if i * a[x] not in numeros:
                numeros.append(i * a[x])
            i += 1
    print(len(numeros))'''

#Questão 25

'''def ppa(a, b):
    if a == 1:
        if b == 1:
            return "Sem ganhador"
        elif b == 2:
            return "Jogador 1 venceu"
        else:
            return "Jogador 2 venceu"
    elif a == 2:
        if b == 1 or b == 3:
            return "Jogador 2 venceu"
        else:
            return "Ambos venceram"
    else:
        if b == 1 or b == 2:
            return "Jogador 1 venceu"
        else:
            return "Aniquilacao mutua"'''

#Questão 26

'''def somarCord(a, b, c):
    return int(a) + int(b) + int(c)
valores = []
for i in range(int(input())):
    a, b, c = input().split()
    valores.append(somarCord(a, b, c))
if sum(valores) == 0:
    print("YES")
else:
    print("NO")'''

#Questão 27

'''primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47,53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]
def ehPrimo(a):
    if a in primos:
        return 1
    else:
        return 0
def divisoresPrimos(a):
    if a not in primos:
        contador = 0
        i = 0
        while primos[i] < a:
            if a % primos[i] == 0:
                contador += 1
            i += 1
        print(contador)'''

#Questão 32
'''verifica = True
numeros = []
while verifica:
    aux = int(input())
    if aux != -1:
        numeros.append(aux ** -1)
    else:
        verifica = False
print(int(len(numeros)/sum(numeros)))'''

#Questão 33
'''lista = input().split()
lista.pop(len(lista) - 1)
print(' '.join(map(str, list(reversed(lista)))))'''

#Questão 34
'''def encontraIndice(lista, tamanho):
    for i in range(len(lista)):
        if lista[i] <= tamanho:
            return lista.index(lista[i])
    return -1
bill = int(input())
aux = input().split()
tamanhos = sorted(list(map(int, aux)))
encontraIndice(tamanhos, bill)'''

#Questão 35
'''palavra = input()
if "-" not in palavra:
    print(palavra[::-1])
else:
    palavra = palavra.strip()
    print(f'-{palavra[::-1]}')'''

#Questão 36
'''def remove_duplicatas(x):
    limpo = []
    for i in range(0, len(x)):
        if x[i] not in limpo:
            limpo.append(x[i])
    return limpo'''

#Questão 37
'''print('c' > 'b')'''

#Questão 11
'''palavra = input()
print(palavra.upper())'''


#Questão 10
'''for x in range(0, int(input())):
    lista = input()
    result = ''
    letra = ''
    numero = 0
    i = 0
    while i < len(lista):
        if lista[i].isnumeric() == False:
            letra = lista[i]
            i += 1
        else:
            while lista[i].isnumeric():
                numero = numero * 10 + int(lista[i])
                i += 1
                if i > len(lista):
                    break
            result += letra * numero
            numero = 0
    print(result)'''

#Questão 3
'''vet = []
numero = int(input())
soma = 0
for i in range(2):
    vet.append(list(map(int, input().strip().split())))
for j in range(0, numero):
    soma += vet[j][j] * vet[j + 1][j]
if soma == 0:
    print('ortogonais')
else:
    print(soma)'''
    
#Questão 18
n = int(input())
def sinuquera(n):
    n -= 1
    i = 1
    soma = 0
    while i < n:
        soma += 1
        i += 1
        n -= 1
    return soma

def sinuquera(n):
    if n != 1 and n % 2 == 0:
        return int((n / 2) - 1)
    elif n != 1 and n % 2 == 1:
        return int(((n - 1)/2))
    else:
        return 0
