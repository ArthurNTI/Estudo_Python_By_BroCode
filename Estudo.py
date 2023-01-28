# ESTUDO DE VARIAVEIS E CONCATENACAO#
# pnome = "aratu"
# unome = "buei"
# fnome = pnome +" "+ unome
# print("hello "+fnome)

# idade = 9
# idade += 1
# print("Sua idade é :"+str(idade))

# altura = 178.5
# print("Sua altura é : "+str(altura)+("cm"))
# print(type(altura))

# humano = True
# print("Voce e humano ? "+str(humano))
# print(type(humano))

# FIM#

# MULTIPLE ASSIGMENTS#
# nome,idade,altura = "arthur", 18, 178.5

# print(nome)
# print(idade)
# print(altura)

# p1 = 12
# p2 = 12
# p3 = 12

# Em casos que as variaveis possuem o mesmo valor voce pode fazer assim : p1 = p2 = p3 = 12

# FIM#

# STRING METODS#

# nome = "Aratu"
# print(len(nome)) : Tamanho da string
# print(nome.find("a")) : Indica onde esta a letra escolhida
# print(nome.capitalize()) : Transforma em maiusculo a primeira letra
# print(nome.upper()) : Tranforma a string inteira em maiusculo
# print(nome.lower()) : Tranforma a string inteira em minuscula
# print(nome.isdigit()) : Indica se tem ou nao digitos na string
# print(nome.isalpha()) : Indica se tem ou nao letras do alfabeto na string
# print(nome.count("a")) : Conta quantas letras da escolhida tem na string
# print(nome.replace("A","O")) : Troca uma letra escolhida por outra
# print(nome*3) : Multiplica a quantidade de vezes que a string aparece

# FIM#

# TYPE CAST#

# a = 1
# b = 2.3
# c = "3"

# a = float(a) : Tranforma em float
# b = str(b) : Tranforma em string
# c = int(c) : Tranforma em int

# print(a)
# print(b)
# print(c)

# FIM#

# USER INPUT#

# name = input("Digite seu nome : ")
# print("Eae " + name, "meu caro")
# idade = int(input("Digite sua idade " + name + " :"))

# print("Ola " + name)
# print("Voce tem " + str(idade) + " anos de idade !")

# FIM#

# MATH FUNCTIONS#

# import math #Biblioteca para funcoes matematicas

# pi  = 3.14
# a = 1
# b = 2
# c = 3

# print(round(pi)) #Arredonda o valor para o numero inteiro mais proximo
# print(math.ceil(pi)) #Arredonda para cima o valor
# print(math.floor(pi)) #Arredonda para baixo o valor
# print(abs(pi)) #Indica o quao distante esta o numero de 0
# print(pow(pi,3)) #Funcao para exponenciacao, (base,expoente)
# print(math.sqrt(9)) #Funcao para pegar a raiz quadrada de um numero
# print(max(a,b,c)) #Indica o maior valor entre as variaveis
# print(min(a,b,c)) #Indica o menor valor entre as variaveis

# FIM

# SLICING STRINGS#

# Indexing function[start;stop;step]
# nome = "artu buei"
# pnome = nome[:3] #Pegar string apartir de um ponto exclusivo [inicio:fim] sendo que, inicio é inclusivo e fim é exclusivo.
# unome = nome[5:]
# tnome = nome[:9:2] #Pega de 2 em 2 caracteres da string
# fuckname = nome[::-1] #Reverte o nome
# print(fuckname)

# Slicing function
# slice = slice(7,-4) #Funcao para cortar uma determinada parte da string, (inicio,fim), o fum conta da direita pra esquerda como valor negativo

# website = "http://google.com" #site exemplo
# website2 = "http://wikipedia.com"#site exemplo 2

# print(website[slice]) #print(nomeexemplo[slice])
# print(website2[slice]) #print(nomeexemplo[slice]) 2

# FIM#

# Continha exercicio aleatorio
# alt = int(input("insira a altura de um quadrado :"))
# ar = int(input("insira a largura de um quadrado :"))

# conta1 = alt * lar
# conta2 = (pow(conta1,2))

# print(conta2)

# FIM

# IF STATEMENTS#

# age = int(input("How old are you ?"))

# if age >= 18:
#   print("You are an adult")

# elif age <= 0:
#    print("You haven't been born yet")

# else:
#    print("You aren't an adult")

# FIM#

# EXERCICIO IF STATEMENT#

# Questao 1: Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

# letra = input("Digite uma letra e sera dito se é consoante ou vogal : ")

# if (letra == 'a') or (letra == 'e') or (letra == 'i') or (letra == 'o') or (letra == 'u' ):
#    print("A letra digitada é uma vogal !")

# else: print("A letra digitada não é uma vogal")

# FIM#

# Questao 2: Faça um Programa que leia três números inteiros e mostre o maior deles.

# print("Insira 3 numero inteiros e sera dito qual o maior entre eles :")
# um1 = int(input())
# num2 = int(input())
# num3 = int(input())

# if (num1 > num2) and (num1 > num3):
#    print("O primeiro numero digitado é o maior !")

# if (num2 > num1) and (num2 > num3):
#    print("O segundo numero digitado é o maior !")

# if (num3 > num2) and (num3 > num1):
# print("O terceiro numero digitado é o maior !")

# Operador NOT: O operador not inverte o retorno da funcao, se TRUE retornara FALSE
# Demonstracao de aplicacao:  if not(x>x or x<x):

# Questao 3: Faça um programa que pede dois inteiro e armazene em duas variáveis. Em seguida, troque o valor das variáveis e exiba na tela.

# print("Digite 2 numeros inteiros e sera invertido seus valores !")
# num1 = int(input("Digite o primeiro numero inteiro"))
# num2 = int(input("Digite o segundo numero inteiro"))
# print("Invertendo...")

# aux = num2
# num2 = num1
# num1 = aux

# print(num1)
# print(num2)

'''OU
v1 = input()
v2 = input()


[v1, v2] = [v2, v1]

print(v1)
print(v2)'''

# FIM#

# WHILE LOOPS# "repeticao sem limite"

# while 1==1:
#   print("Help i am stuck in a loop")

# name = ""

# while len(name) == 0:
#    name = input("Digite seu nome :")

# print("Hello " +name+ " You are biutiful")

# FIM#

# FOR LOOPS# "repeticao com limite"

# for i in range (10):
#    print (i+1)

# for i in range (40,100): # for i in range (inicio(inclusivo),fim(exclusivo),step)
#   print(i)

# for i in 'aratu':
#    print(i)

# import time

# for seconds in range(10, 0, -1):
#    print(seconds)
#    time.sleep(1)

# print("Parabens vc e buei")

# FIM#

# Nested loops#

# linhas = int (input ("Insira o numero de linhas desejadas :"))
# colunas = int (input ("Insira o numero de colunas desejadas :"))
# simbolo = input ("Insira o simbolo para o preenchimento")

# for i in range (linhas):
#    for j in range (colunas):
#        print (simbolo, end="")
#    print ( )

# FIM

# BREAK AND CONTINUE AND PASS#

# break = Para totalmente o loop
# continue = Pula para a proxima acao do loop
# pass = Faz nada, apenas ocupa um espaço

# while True:
#    name = input("Digite seu nome : ")
#    if name != "":
#        break

# Opcao continuar#

# while True:
#    fim = int(input("1 para sair 2 para continuar :"))
#    if fim == 1 :
#        print("Adios hermano")
#        break
#    elif fim == 2 :
#       continue

# phonenumber = "8-8-8-8-8888"
# for i  in phonenumber:
#    if i == "-":
#        continue
#    print(i,end="")

# for i in range(1,21):
#    if i == 13:
#        pass
#   else:
#       print(i)

# FIM#

# LISTS#

# comida = ["Arroz","Feijao","Carne","Pizza"]

# comida[0] = "amigao"

# comida.append("Coisa boa") #Adiciona string desejada
# comida.remove("Arroz") #Remove a string selecionada
# comida.pop() #Remove a ultima string
# comida.insert(0,"Ice") #Insere a string desejada no local desejado
# comida.sort() #Organiza em ordem alfabetica as strings
# comida.clear() #Limpa todas as strings

# for i in (comida):
#    print(i)

# FIM#

# 2D LISTS#

# sucos = ("Laranja","Limao","Abacaxi")
# lanches = ("Hamburger","Pizza")
# salgados = ("Coxinha","Pastel")

# comidas = (sucos,lanches,salgados)

# print(comidas)

# FIM#

# TUPLES #

# pessoa = ("aratu",18,"M")

# print(pessoa.count("aratu"))
# print(pessoa.index("M"))

# for i in pessoa:
#    print(i)

# if 'aratu' in pessoa:
#    print("Aratu é buei !")

# FIM #

# SETS # # Desanexados, nao possem ordem e nao pode ser duplicado.

# utensilios = {"Garfo", "Faca", "Colher"}
# louças = {"Prato", "Copos", "Vasilia","Faca"}

# utensilios.add("Foice") #Adiciona uma string
# tensilios.remove("Garfo") #Remove uma string
# utensilios.clear() #Limpa tudo
# utensilios.update(louças) #Adiciona um set no outro
# mesa = utensilios.union(louças) #Une dois sets em um
# print(utensilios.difference(louças)) #Indica oque utensilios tem que a loucas nao tem, diferenca
# print(utensilios.intersection(louças)) #Indica oque os sets tem em comum

# for i in mesa:
#    print(i)

# FIM #

# DICTIONARIES # = Variavel, desordenada colecao de chaves, key:values

# capitais = {'USA':'Whashington',
#            'India':'Nova Dehli',
#            'China':'Beijing',
#            'Russia':'Moscow'}

# capitais.update({'Germany':'Berlin'}) #Adiciona uma key e um value para o dicionario
# capitais.update({'USA':'Las Vegas'}) #Atualiza o value de uma key existente
# capitais.pop('China') #Remove uma key por exemplo

# print(capitais['USA']) #Printa um resultado de uma palavra chave
# print(capitais.get('Germany')) #Metodo para buscar uma string no dicionario
# print(capitais.keys()) #Printa as keys do dicionario
# print(capitais.values()) #Printa os values do dicionario
# print(capitais.items()) #Printa todo o dicionario

# or key,value in capitais.items(): #Outra maneira de printar todo o dicionario
#   print (key, value)

# FIM #

# INDEXING #

# nome = 'aratu almida !'
# pnome = nome[0:5].upper()  # nome[inicio(inclusivo):fim(exclusivo)]
# unome = nome[6:].capitalize() # nome[inicio(inclusivo):fim(exclusivo)]
# cnome = pnome+' '+unome #Juntou as duas partes do nome
# lcharacter = nome[-1] #Printa o ultimo caractere

# if (nome[0].islower()):
#    nome = nome.capitalize()

# print(cnome)

# FIM #

# FUNCTIONS #

# def ola(name, lname, idade):
#   print("Ola "+name+' '+lname)
#    print("Voce tem "+str(idade)+" anos de idade !")

# ola('Artu', 'Cuei', 18)

# FIM #

# RETURN STATEMENT #

# def mult(v1,v2):
#   resultado = v1*v2
#    return resultado

# x = mult(2,4)

# print(x)

# FIM #

# KEWWORD ARGUMENTS # = Consegue alterar a ordem dos argumentos recebidos pela funcao

# def name(pnome,mnome,lnome):
#    print("Hello "+pnome+' '+mnome+' '+lnome)

# name(mnome="artu",lnome="Almida",pnome="Kinot")

# FIM #

# NESTED FUNCTION CALLS # : Funcao dentro de funcao, algumas funcoes retornam valores, logo, isso se torna possivel.

# print(round(abs(float(input("Digite um numero :")))))


# num = float(num)
# num = abs(num)
# num = round(num)
# print(num)

# FIM #

# Scope #  : A região onde uma variavel é reconhecida, a variavel só é disponivel onde foi criada.

# nome = "Almida"

# def mostrar_nome():
#    nome = "Aratu"  #Local scope, só existe dentro da função.
#    print(nome)

# mostrar_nome()
# print(nome)

# fIM #

# arguments (*args) #  : parametro que vai juntar todos os argumentos em uma tupla, util para que a função possa aceitar uma quantidade variavel de argumentos.

# Tuplas :Tupla é um tipo de estrutura de dados utilizada em Python que funciona de modo semelhante a uma lista, entretanto,
# com a característica principal de ser imutável. Isso significa que quando uma tupla é criada não é possível adicionar, alterar ou remover seus elementos.

# Tuple é como uma lista, a diferença é que tuples são imutaveis


# def add(num1,num2):
#    sum = num1 + num2
#    return sum

# print(add(1,2,3)) #Nesse caso o codigo nao aceitaria, pois voce esta mandando 3 argumentos, e a função aceita somente 2.

# def add(*args):
#    sum = 0
#    for i in args:
#        sum += i
#   return sum

# print(add(1,2,3))

# def add(*stuff):
#    sum = 0
#   stuff = list(stuff)
#    stuff[0] = 0
#    for i in stuff:
#        sum += i
#    return sum

# print(add(1,2,3,4,5,6))

# FIM #

# **kwargs = parametro que empacota todos os argumentos em um dicionario, util quando uma função pode aceitar uma quantidade variavel de keyword arguments.

# def hello(**kwargs):
# print("Hello " + kwargs['primeiro'] + " " + kwargs["ultimo"])
#    print("Hello",end = ' ')
#    for key,value in kwargs.items():
#        print(value,end = ' ')   # end = ' ' Imprime as strings na mesma linha

# hello(primeiro="Artu", meio="de", ultimo="Almida", amem="bei", pastel = 'dale')

# FIM #

# str.string() = Método ideal que oferece aos usuários mais controle ao exibir a saída

# import os
# animal = 'vaca'
# item = 'lua'

# print('A '+animal+' pulou sobre a '+item)
# print('A {} pulou sobre a {}'.format(animal,item)) #Recebe por ordem, argumento posicional
# print('A {1} pulou sobre a {0}'.format(animal,item)) #Recebe por ordem, argumento posicional
# print('A {animal} pulou sobre a {item}'.format(animal='vaca',item='lua')) #kewword argument

# name = "artu"
# print("Hello, my name is {}".format(name))
# print("Hello, my name is {:10}".format(name)) #Deixa 10 espaços após a variavel
# print("Hello, my name is {:<10}".format(name)) #Mesma coisa que o de cima
# print("Hello, my name is {:>10}".format(name)) #Deixa 10 espaços antes da variavel
# print("Hello, my name is {:^10}".format(name)) #Centraliza com a quantidade de espaços escolhida

# n1 = 1000

# print("O numero de pi é : {:.2f}".format(n1)) #Delimita quantas casas aparecem da variavel selecionada "{:.2f}"
# print("O numero de pi é : {:,}".format(n1)) #Printa o numero em formato inteiro
# print("O numero de pi é : {:b}".format(n1)) #Printa o numero em formato binario
# print("O numero de pi é : {:o}".format(n1)) #Printa o numero em formato octal
# print("O numero de pi é : {:x}".format(n1)) #Printa o numero em formato hexadecimal
# print("O numero de pi é : {:E}".format(n1)) #Printa o numero em formato de notação cientifica

# FIM #

# Pseudo random #

# import random

# x = random.randint(1,6) #Entrega um valor inteiro entre a delimitação escolhida
# y = random.random() #Entrega um valor flutuante entre a delimitação escolhida

# lista = ['pedra','papel','tesoura'] #Exemplo de lista com strings
# z = random.choice(lista) #Entre um valor aleatorio de string.

# cartas = [1,2,3,4,5,6,7,'j','k','l','m'] #Exemplo de lista
# random.shuffle(cartas) #Embaralha tudo oque tem dentro de uma lista

# print(cartas)

# FIM #

# Exeption # : eventos detectados durante a execução de um programa que interrompe o fluxo de um programa

# try:
#    numerador = int(input('Insira um numero inteiro para ser o numerador : '))
#    denominador = int(input('Insira um numero inteiro para ser o denominador : '))
#    resultado = numerador/denominador
#    print(resultado)

# except ZeroDivisionError:
#    print('Divisão com o denominador 0 é uma indeterminação')

# except ValueError:
#    print("Digite somente numeros!")

# except ValueError as e:  # Alternativa opcional para demonstrar qual foi o erro 'as e' + 'print(e)'
#    print(e)
#    print("Digite somente numeros!")

# except Exception:
#    print('Algo deu errado :(')

# else:
#    print(resultado)

# finally:
#    print("Isso sempre vai executar !!!")

# FIM #

# File detection # : \\ = barra invertida


# path = "C:\\Users\\Aratu\\desktop\\teste" #Caminho de um arquivo dentro de uma variavel

# if os.path.exists(path):  #Verifica se o arquivo existe
#    print('O arquivo '+(path)+' existe !')

#    if os.path.isfile(path): #Verifica se é um arquivo
#        print("Isso é um arquivo")

#    elif os.path.isdir(path): #Verifica se é um diretorio
#        print("Isso é um diretorio")
# else:
#    print("Esse arquivo não existe !")

# FIM #

# Read a file #

# try:
#    with open('teste.tx') as file: #Comandos para ler um arquivo
#        print(file.read())

# except FileNotFoundError: #Except para arquivo nao encontrado erro
#    print('O arquivo não foi encontrado')

# print(file.closed) #Se retornar True, o arquivo foi fechado, se False o arquivo esta aberto

# FIM #

# Write a file #

# texto = "Hello buei\nThis is some text"

# with open('teste.txt','w') as file:
#    file.write(texto)

# FIM #

# Copy a file #

# copyfile() = copia o conteudo de um arquivo
# copy() = copyfile() + permission mode + destination can be a directory
# copy2() = copy() + copies metadata (files's creation and modification times)

# import shutil

# shutil.copyfile('teste.txt','copia.txt') #src.dst  #('nome do arquivo que deseja copiar','nome do arquivo novo')

# FIM #

# Move a file #

# import os #Biblioteca para ter acesso as funções de navegação nos arquivos

# fonte = "pasta"
# destino = "C:\\Users\\Aratu\\Desktop\\pasta"

# try:
#    if os.path.exists(destino):
#        print("Existe um arquivo")
#    else:
#        os.replace(fonte, destino)
#        print(fonte+" foi movido !")

# except FileNotFoundError:
#    print(fonte + " não foi encontrado")

# FIM #

# Delete a file #

# import os
# import shutil

# fonte = 'empty_folder'

# try:
# os.remove('fonte')
# print('O arquivo '+fonte+(' foi removido'))
# shutil.rmtree(fonte) #"Remove three", apaga tudo oque for selecionado, mesmo se a pasta tiver conteudo dentro
# os.rmdir(fonte)  # Remove pasta ser conteudo dentro

# except FileNotFoundError:
#    print('O arquivo não foi encontrado')

# except PermissionError:
#    print('Permissao nao consedida')

# except OSError:
#    print('Não é possivel deletar pasta pois tem conteudo dentro')

# else:
#    print(fonte+' foi deletado')

# FIM #

# Module # #Permite separar o programa em partes

# import mensagens   #Chama funcoes de outro modulo
# import mensagens as msg   #Renomeia a função desejada.
# from mensagens import ola,tchau   #Dessa forma as funcoes do outro modulo estarão diretamente no modulo em que foi chamado
# from mensagens import *   #Importa todas as funcoes do outro modulo " * "
# help("modules")    #Mostra todos os módulos disponiveis

# ola()
# tchau()

# FIM #

# Pedra, papel e tesoura JOGO #

'''   import random
escolhas = ["pedra","papel","tesoura"]
jogador = None
computador = random.choice(escolhas)

while jogador not in escolhas:
    jogador = input("pedra, papel ou tesoura? :").lower()

if jogador == computador:
    print("Empate")
    print('computador :',computador)
    print('jogador :',jogador)

elif jogador == "pedra":
    if computador ==  "papel":
        print('computador :', computador)
        print('jogador :', jogador)
        print('Voce perdeu !')

elif jogador == "pedra":
    if computador == "tesoura":
        print('computador :', computador)
        print('jogador :', jogador)
        print('Voce ganhou !')

elif jogador == "tesoura":
    if computador == "papel":
        print('computador :', computador)
        print('jogador :', jogador)
        print('Voce ganhou !')

elif jogador == "tesoura":
    if computador == "pedra":
        print('computador :', computador)
        print('jogador :', jogador)
        print('Voce perdeu !')

elif jogador == "papel":
    if computador == "pedra":
        print('computador :', computador)
        print('jogador :', jogador)
        print('Voce ganhou !')

elif jogador == "papel":
    if computador == "tesoura":
        print('computador :', computador)
        print('jogador :', jogador)
        print('Voce perdeu !')   '''

# FIM #


# TENTAR DIMINUIR CODIGO ACIMA COM FUNCOES !!!


# QUIZ GAME #

print('Doidera !!')