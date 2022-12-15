'''import math

#Atividade 1
#Não pode ficar escrevendo coisas a mais >:cc

car = input("Digite um caractere: ")
print(car)
print(car * 2)
print("%s %s" % (car, car))
print("2%s" % car)
print("[%s]" % car)
#Esse tipo de formatação de string consiste em colocar entre aspas alguns códigos que eventualmente serão substituidos por variáveis, por exemplo ("%d" % num). Alguns códigos são:
#%d - apresenta a variável NUMÉRICA em forma de inteiro; %f - apresenta a variável NUMÉRICO como ponto flutuante; %s - apresenta a variável como string.


#Atividade 2

car1 = input()
car2 = input()
car3 = input()
print("%s%s%s" % (car1, car2, car3))
print(car1)
print("%s%s" % (car2, car2))
print("%s %s %s" % (car3, car3, car3))
print("X == %s, Y == %s, Z == %s" % (car1, car2, car3))
print("X != %s, Y != %s, Z == %s" % (car2, car1, car3))

#Atividade 3
def desenha():
    print('+ - - - - + - - - - +')
    print('|         |         |')
    print('|         |         |')
    print('|         |         |')
    print('|         |         |')
    print('|         |         |')
    print('+ - - - - + - - - - +')
    print('|         |         |')
    print('|         |         |')
    print('|         |         |')
    print('|         |         |')
    print('|         |         |')
    print('+ - - - - + - - - - +')

desenha()

def faz_dois(f):
    f()
    f()

def faz_quatro(f):
    faz_dois(f)
    faz_dois(f)

def faz_partemais():
    print('+ - - - -', end=' ')

def faz_partebarra():
    print('|        ', end=' ')

def print_linhamais():
    faz_dois(faz_partemais)
    print('+')

def print_linhabarra():
    faz_dois(faz_partebarra)
    print('|')

def desenha():
    print_linhamais()
    faz_quatro(print_linhabarra)
    print_linhamais()
    faz_quatro(print_linhabarra)
    print_linhamais()

desenha()

def imprimeAPC():
    print('    _    ____   ____ ')
    print('   / \  |  _ \ / ___|')
    print('  / _ \ | |_) | |    ')
    print(' / ___ \|  __/| |___ ')
    print('/_/   \_\_|    \____|')

#Atividade 4
#Tem que importar Math antes
ler = input()
base = float(ler[0])
exp = float(ler[2])
print(math.pow(base, exp))
#Aqui usamos a função math.pow() pra descobrir a potência, né, mas num tinha necessidade pq dá pra escrever isso como x ** y que é A MESMA COISA

#Atividade 5
#tomanocunessaporra
ler = input()
base = float(ler[0])
exp = float(ler[2])
def powAPC(x, y):
    print(math.pow(x, y))
powAPC(base, exp)
#Aqui é pra ver se a gente sabe fazer função e talz, somo muito bom

#Atividade 6
def converte(x):
    x = float(x)
    celsius = (x - 32)/1.8 #converte celsius para farenheit é isto
    print('%2.1f' % celsius) 

converte(-1.0)  

#Atividade 7
def converte(x):
    x = float(x)
    faren = (9 * x)/5 + 32 #converte farenheit para celsius uou
    print('%2.1f' % faren)

converte(1)

#Atividade 8
dinheiro = input()
du, dudu, edu = dinheiro.split(" ")
du = float(du)
dudu = float(dudu)
edu = float(edu)
soma = du + dudu + edu
#Aqui vamos usar a f-string para formatar o 'print' uhul
print(f'{1.1 * du:.2f} {1.1 * dudu:.2f} {1.1 * edu:.2f}') #Cada variável será apresentada com a formatação em ponto flutuante e com duas casas após a virgula
print(f'{1.1 * soma:.2f}') #do mesmo modo, a variável 'soma' será apresentada como ponto flutuante com duas casas decimais após a vírgula

#Atividade 9
ler = float(input())
diametro = ler * 2
area = 3.14159 * ler ** 2 #O valor de PI nos foi dado no exercício, mas também poderiamos usar Math.pi para obter um valor mais preciso
perimetro = diametro * 3.14159
print(f'{diametro:.2f}')
print(f'{area:.2f}')
print(f'{perimetro:.2f}')

#Atividade 10
dia, mes, ano = input().split("/") #A string que vamos receber no input tem seus valores separados por uma barra, então dentro da função 'split' colocamos essa barra como parâmetro para separar os valores da string adequadamente ><
print("%s-%s-%s" % (dia, mes, ano))
print("%s-%s-%s" % (mes, dia, ano))
print("%s/%s/%s" % (ano, mes, dia))

#Atividade 11
for i in range(5):
    num1, num2 = input().split()
    num1 = int(num1)
    num2 = int(num2)
    def maiorAB(A, B):
        print(max(A, B)) #A função MAX retorna o maior valor entre dois números
    maiorAB(num1, num2)

#Atividade 12
def trocarAB(a, b):
    print(b, a)

for i in range(5):
    a, b = [int(x) for x in input().split()] #transforma em int os valores recebidos do input().split()
    trocarAB(a, b)'''

a, b, c = [int(x) for x in input().split()]
print(a, b, c)