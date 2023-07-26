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

# STRING METHODS#

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
# fuckname = nome[::-1] #Inverte o nome
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

# Sets #  Desanexados, nao possuem ordem e nao pode conter valores duplicados.

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
'''
#--------------------
def novo_jogo():
    palpites = []
    palpites_corretos = 0
    questao_numero = 1

    for key in questoes:
        print("--------------------")
        print(key)
        for i in opcoes[questao_numero-1]:
            print(i)
        palpite = input("Escolha (A,B,C ou D): ")
        palpite = palpite.upper()
        palpites.append(palpite)

        palpites_corretos += checar_resposta(questoes.get(key),palpite)
        questao_numero += 1    

    mostrar_pontuacao(palpites_corretos, palpites)
#--------------------
def checar_resposta(palpites_corretos, palpite):
    
    if palpites_corretos == palpite:
        print("Correto !")
        return 1
    else:
        print("Errado !")    
        return 0
#--------------------
def mostrar_pontuacao(palpites_corretos, palpites):
    print("---------------")
    print("RESULTADOS")
    print("---------------")

    print("Respostas: ", end=" ")
    for i in questoes:
        print(questoes.get(i),end=" ")
    print()

    print("Perguntas: ", end="")
    for i in palpites:
        print(i,end=" ")
    print()

    pontuacao = int((palpites_corretos/len(questoes)*100))
    print("Sua pontuacão é: "+str(pontuacao)+"%")
#--------------------
def jogar_novamente():

    resposta = input("Voce deseja jogar novamente ? (sim ou nao) :")
    resposta = resposta.upper()

    if resposta == "SIM":
        return True
    else: 
        return False
#--------------------

questoes = {
    "Quem criou o Python ?: " : "A",
    "Que ano o Python foi criado ?: " : "B",
    "Python foi uma homenagem a que grupo de comédia ?: " : "C",
    "A terra é redonda ?: ": "A"
}

opcoes = [["A. Guido Van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerburg"],
    ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
    ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
    ["A. Verdadeiro", "B. Falso", "C. As vezes", "D. O que é Terra ?"]]

novo_jogo()

while jogar_novamente():
    novo_jogo()

print("Adeus")    
    
'''

# FIM #

# OBJECT ORIENTED PROGRAMMING # (OOP)
'''
class Car: #Car tera um C maiusculo #Se criar uma classe em outro modulo tera que chamar com uma funcao. Exemplo : "from car import Car"
    

    def __init__(self,fazer,modelo,ano,cor):
        self.fazer = fazer
        self.modelo = modelo
        self.ano = ano
        self.cor = cor

    def dirigir(self):
        print("Esse "+self.modelo+" esta em movimento")

    def parar(self): 
        print("Esse "+self.modelo+" esta parado")    


carro_1 = Car("Chevy","Corvette","2021","blue")
carro_2 = Car("Ford","Mustang","2022","red")

#print(carro_2.fazer)
#print(carro_2.modelo)
#print(carro_2.ano)
#print(carro_2.cor)

carro_1.dirigir()
carro_2.parar()
'''

# FIM #

# Class variable #
'''
class Car:

    rodas = 4 #Variavel de classe

    def __init__(self,fazer,modelo,ano,cor):
        self.fazer = fazer #Varivavel de instancia
        self.modelo = modelo #Varivavel de instancia
        self.ano = ano #Varivavel de instancia
        self.cor = cor #Varivavel de instancia

    def dirigir(self):
        print("Esse "+self.modelo+" esta em movimento")

    def parar(self): 
        print("Esse "+self.modelo+" esta parado")    


carro_1 = Car("Chevy","Corvette","2021","blue")
carro_2 = Car("Ford","Mustang","2022","red")


#print(carro_2.rodas)
#print(Car.rodas)
'''

# FIM #

# Inheritance # : Herança
'''
class Animais: #Criando classe, sempre o inicio do nome na classe letra maiuscula

    vivo = True

    def comendo(self): #Funcoes globais
        print("Esse animal esta comendo ")
    def dormindo(self): #Funcoes globais
        print("Esse animal esta dormindo ")    

class Coelho(Animais): #Dessa forma cada classe pode ter suas funcoes separadamente
    def correr(self):
        print("Esse animal esta correndo")

class Peixe(Animais): 
    def nadar(self):
        print("Esse animal esta nadando")

class Aguia(Animais):
    def voar(self):
        print("Esse animal esta correndo")

coelho = Coelho()
peixe = Peixe()
aguia = Aguia()

print(coelho.vivo)
peixe.comendo()
aguia.dormindo()
'''

# FIM #

# Multiple level Inheritance # : Heranca entre mais de uma classe

'''
class Organismo:
    vivo = True

class Animal(Organismo):    
    
    def eat(self):
        print("Esse animal esta comendo")

class Cachorro(Animal):

    def latindo(self):
        print("Esse cachorro esta latindo")        

cachorro = Cachorro()
print(cachorro.vivo)
cachorro.eat()
cachorro.latindo()
'''

# CONTINUA ABAIXO # Heranca acontecendo mais de 2 vezes

'''
class Presa:

    def fugir(self):
        print("Esse animal foge")

class Predador:

    def caça(self):
        print("Esse animal caça")

class Coelho(Presa):
    pass

class Aguia(Predador):
    pass

class Peixe(Predador,Presa):
    pass

coelho = Coelho()
aguia = Aguia()
peixe = Peixe()

coelho.fugir()
aguia.caça()
peixe.caça()
peixe.fugir()
'''

# Method overriding # : Metodo de substituicao, funciona matematicamente como parenteses,
# sempre oque esta mais a dentro tem a prioridade

'''
class Animal:
    def comer(self):
        print("Esse animal esta comendo")

class Coelho(Animal):
    def comer(self):
        print("Esse animal come cenouras")

coelho = Coelho()
coelho.comer()
'''

# FIM #


# Method chaining # :Encadeamento de método
'''
class Carro:

    def ligar(self):
        print("Voce ligou o carro")
        return self

    def dirigir(self):
        print("Voce esta dirigindo o carro")  
        return self

    def freiar(self):
        print("Voce esta freiando o carro") 
        return self

    def desligar(self):
        print("Voce esta desligando o carro")  
        return self

carro = Carro()   

#carro.ligar() #Normalmente seria feito dessa maneira.
#carro.dirigir()

#carro.ligar().dirigir() #Para encadeamento de metodos é necessario dentro da função adicionar
# "return self", dessa forma seria como se voce estivesse digitando carro.ligar(),carro.dirigir()

#carro.freiar().desligar()
carro.ligar().dirigir().freiar().desligar()
'''

# FIM #

# Super function # : Funcao usada para ter acesso aos metodos de uma classe superior

'''
class Retangulo:

    def __init__(self, largura,altura):
        self.largura = largura
        self.altura =altura
    
class Quadrado(Retangulo):
    def __init__(self, largura,altura):
        super().__init__(largura,altura)

    def area(self):
        return self.largura*self.altura

class Cubo(Retangulo):
    
    def __init__(self,largura,altura,grossura) :
        super().__init__(largura,altura)
        self.grossura = grossura

    def volume(self):
        return self.largura*self.altura*self.grossura

quadrado = Quadrado(3, 3)
cubo = Cubo(3, 3, 3)

print(quadrado.area())
print(cubo.volume())
'''

# Abstract Classes #  :Uma classe que contém um ou mais métodos abstratos
'''

from abc import ABC, abstractmethod
class Veiculo(ABC):

    @abstractmethod  # Metodos abstratos previnem de em alguma clase herdeira ficar devendo requisitos, previnir que "child" classes nao estao faltando implementacoes que elas herdam
    def ir(self):
        pass

    @abstractmethod  # Usando esse metodo voce garante que as outras classes herdeiras nao estao faltando implementacoes, 'same as above but with ma words'
    def parar(self):
        pass


class Carro(Veiculo):

    def ir(self):
        print("Voce esta dirigindo o carro")

    def parar(self):
        print("Esse carro esta parado")


class Moto(Veiculo):

    def ir(self):
        print("Voce esta dirigindo a moto")

    def parar(self):
        print("Essa moto esta parada")


# veiculo = Veiculo()
carro = Carro()
moto = Moto()

# veiculo.ir()
carro.parar()
moto.parar()
'''

# FIM #

# Objects as arguments #

'''
class Carro:
    cor = None

class Moto:
    cor = None

def mudar_cor(carro, cor):
    carro.cor = cor

carro_1 = Carro()
carro_2 = Carro()
carro_3 = Carro()

moto_1 = Moto()

mudar_cor(carro_1, "Vermelho")
mudar_cor(carro_2, "Branco")
mudar_cor(carro_3, "Azul")
mudar_cor(moto_1, "Azul")

print(carro_1.cor)
print(carro_2.cor)
print(carro_3.cor)
print(moto_1.cor)
'''

# Exercicio # Deu certo :) same as above but improved

'''
class Carro:
    cor = None

carro = Carro()

carro = input("Qual carro voce deseja selecionar a cor ? :")
cor = input("Qual cor voce deseja ? :")

def mudar_cor(carro, cor):

    carro.cor = cor

print("O carro selecionado foi: "+carro.capitalize()+" e a cor escolhida foi: "+cor.capitalize())
'''

# FIM #

# Duck typing # : é o conceito onde a classe de um objeto que é menos importante que metodos ou atributos, tipo da classe não é checada se os metodos/atributos minimos estão presentes
# "Se anda como um pato, e fala como um pato, provavelmente isso é um pato."
# Se duas classes possuem as mesmas caracteristicas voce consegue chamar ambas em outra classe (foi oque entendi)

'''
class Pato:

    def caminhar(self):
        print("O pato esta caminhando")

    def falar(self):
        print("O pato esta quackando 'quack'")    

class Galinha:
    def caminhar(self):
        print("A galinha esta caminhando")

    def falar(self):
        print("A galinha esta cantando")                  

class Pessoa():
    def catch(self,pato):
        pato.caminhar()
        pato.falar()
        print("Voce pegou o pato")

pato = Pato()
galinha = Galinha()
pessoa = Pessoa()

pessoa.catch(galinha)'''

# FIM #

# Waltus operetor # " := " assigment, atribui valores para variaveis como parte de uma expressao mais longa

# feliz = True
# print(feliz)

# print(happy := True)

#Forma abaixo sem o uso do operador Waltus
'''
comidas = list()
while True:
    comida = input("Que comida voce  gosta ?para sair digite: sair: ")
    if comida == "sair":
        break
    comidas.append(comida)

print(comidas)   
'''
#Codigo sigma abaixo
'''
comidas = list()
while comida := input("Que comida voce gosta ? Ou digite sair para cancelar : ") != "sair":
    comidas.append(comida)
'''

# FIM #

# Function to variables #
'''
def ola():
    print("Ola")
    
oi = ola
oi()
ola()

falar = print
print("Wow")
'''

# High Order Function # : Uma funcao que :        
#                       1. aceita uma funcao como argumento
#                          ou
#                       2. retorna a funcao
#                       (No python, funcoes tambem sao tratadas como objetos)

'''
def alto(text):
    return text.upper()

def baixo(text):
    return text.lower()

def ola(func):
    text = func("Ola")
    print(text)    

ola(baixo)    
ola(alto)    
'''

'''
def divisor(x):
    def dividendo(y):
        return y / x
    return dividendo

dividir = divisor(2) #x
print(dividir(10)) #y
'''

# FIM #

# Lambda fuction # : Funcao escrita em uma linha usando a palavra lambda, aceitar qualquer quantidade de argumentos, mas em apenas uma expressao, (use como um atalho),(util se é necessario para um curto periodo de tempo)
# lambda parametros:expressao

'''
dobrar = lambda x:x * 2
multiplicar = lambda x,y: x * y 
adicionar = lambda x, y, z: x + y + z
nome_completo = lambda primeiro_nome, ultimo_nome: primeiro_nome + " " + ultimo_nome
idade_check = lambda idade:True if idade >= 18 else False
print(idade_check(18))

'''

# FIM #

# sort() method # = usado para listas, metodo para ordenar listas
# sort() function # = usado para iteraveis(iteravel = consegue se multiplicar)
'''
estudantes = ["Arthur","Ana","Ivanete","Danilo","Maria"]

#estudantes.sort(reverse=True)
estudantes_ordenados = sorted(estudantes,reverse=True)

for i in estudantes_ordenados:
    print (i)
'''
'''
familia =    [("Arthur","M","18"),
             ("Ana","F","15"),
             ("Ivanete","F","48"),
             ("Danilo","M","78"),
             ("Maria","F","76")5]

idade = lambda idade:idade[2] 
# familia.sort(key=idade)
sorted_familia = sorted(familia,key=idade)

for i in sorted_familia:
    print(i)
    '''

# Map function # : aplica uma funcao para cada item de uma iteravel(list,tuple,etc...)

# map(function,iterable)
'''
loja = [("camisa",20.00),
        ("calca",15.00),
        ("meias",7.00),
        ("tenis",25.00)]

para_reais = lambda x: (x[0],x[1]*5.20)

loja_reais = list(map(para_reais, loja))

for i in loja_reais:
    print (i)
'''

# FIM 

# Filter fuction : Funcao que retorna apenas os valores true
'''
pessoas = [("Artu",18),
           ("Jacare",15),
           ("Tatu",20),
           ("Alemao",12)]

idade = lambda x : x[1] >= 18
podem_beber = list(filter(idade,pessoas))

for i in podem_beber:
    print(i)
'''

# FIM #

# Reduce function # 


#import functools

'''
letras = ["H","E","L","L","O"]

palavra  = functools.reduce(lambda x, y: x + y, letras)
print(palavra)
'''

'''
fatorial =[5,4,3,2,1]
resultado = functools.reduce(lambda x ,y :x*y, fatorial)
print(resultado)
'''

# FIM #

# Compreensao de lista # : Um metodo para criar uma nova lista com menos sintaxe, consegue imitar algumas funcoes lambda, facil de entender, lista = [expressao for item in iteravel]

'''quadrados = [] #Criando uma lista vazia
for i in range(1,11): #Criando um loop ate um numero delimitado
    quadrados.append(i * i) #Define oque cada loop fara com a funcao, nesse caso, pegar o quadrado do numero descrito pelo loop e adicionar para a lista quadrados
print(quadrados)'''

'''
quadrados = [i * i for i in range(1,11)] 
print(quadrados)
'''

#estudantes = [100,90,80,70,60,50,40,30,20,10,0]

''' Metodo maior, mais linha, menos desempenho
estudantes_aprovados = list(filter(lambda x:x >= 60, estudantes))
print(estudantes_aprovados)
'''

''' Usando novo metodo
estudantes_aprovados = [i for i in estudantes if i >= 60]
print(estudantes_aprovados)
'''

''' Exemplo 2 novo metodo
estudantes_aprovados = [i if i >= 60 else "Desaprovado" for i in estudantes ]   
print(estudantes_aprovados)
'''

# FIM #

# Compreensao de dicionarios # :Um metodo para criar um dicionario usando uma expressao e ele pode fazer o papel de for loops e algumas funcoes lambda. 
# dictionary = {key: (expression) for (key,value) in iterable}

"""
cidades_em_fahrenheit = {'Nova Iorque': 32,
                        'Boston': 75,
                        'Los Angeles' : 100 ,
                        'Chigaco' : 50}

cidades_em_graus = {key: round((value-32)*(5/9)) for (key,value) in cidades_em_fahrenheit.items()}

print(cidades_em_graus)
"""

"""
clima_cidades = {'Nova Iorque': 0, 'Boston': 24, 'Los Angeles': 38, 'Chicado': 10}

cidades_ensolaradas = {key: ("Quente" if value >= 25 else "Frio") for (key,value) in clima_cidades.items()}

print(cidades_ensolaradas)
"""
'''
def check_temp(value): 
    if value >= 22:
        return "Quente"
    elif 69.8>= value >= 4:
        return "Morno"
    else: 
        return "Frio"

clima_cidades = {'Nova Iorque': 0, 'Boston': 24, 'Los Angeles': 38, 'Chicado': 10}
cidades_ensolaradas = {key: check_temp(value) for (key,value) in clima_cidades.items()}

print(cidades_ensolaradas)
'''

# FIM #

# Zip Function # : A funcao zip ira agregar elementos de uma ou mais iteraveis(lists,tuples,sets,etc...) 
# Essa funcao ira criar um objeto zip com elementos emparelhados armazenando os em um tuple para cada elemento dentro de um objeto zip
# zip(*iterables)

'''
usernames = ["Arthur","Jailson","Jare"]
passwords = ("p@ssword","abc123","Guest")
data_login = ["17/11/2004","30/06/2007","1/1/2023"]

users = zip(usernames,passwords,data_login)

for i in users:
    print (i)
'''

# FIM #

# if _name__ == '__main__': : Metodo para saber em qual modulo esta operando o programa

#import modulo_2

#print(__name__)
#print(modulo_2.__name__)

'''
if __name__ == '__main__':
    print("Esse programa esta operando diretamente neste modulo")

else: 
    print("Esse programa esta rodando indiretamente em outro modulo")
    '''

#def hello():
#    print("Hello")

# FIM #

# Time Module #
# Epoch : a data e o tempo que o computador mede o tempo do sistema

#import time 

#print(time.ctime(0)) #Para encontrar o epoch do seu sistema, esse metodo ira converter o tempo que inicialmente é em segundos e converter para uma string legivel, obsÇ nao entendi muito bem a utilidade

#print(time.time( )) #Retorna os segundos atuais desde o epoch

#print(time.ctime(time.time()))


#time_object = time.localtime() #Data/tempo
#time_object = time.gmtime() #UTC time
#print(time_object) #
#local_time = time.strftime("%B %d %Y %H:%M:%S", time_object) #Printando data tempo horario bonito
#print(local_time)

#time_string = "2 Fevereiro, 2022"
#time_object = time.strptime(time_string,"%d %B, %Y")
#print(time_object)

# FIM #

# Output colorido #

'''
from colorama import Fore

print(Fore.BLUE+"Hello World !")
'''

# FIM #

# Threading #  : Neste exemplo a função main tem o papel de criar mais 3 threads, e assim há a possibilidade de seccionar cada função para um trhead, 
#                elas rodam simultateamente mas não em paralelo

# cpu bound = programa/tarefa que ocupa maior parte do seu tempo esperando por eventos internos (CPU intensive)
#             use multiprocessamento 

# io bound = programa/tarefa que ocupa maior parte do tempo esperando por eventos externos (User input)
#            use multithreading


"""
import threading
import time

def eat():
    time.sleep(3)
    print("You eat breakfast")

def drink():
    time.sleep(4)
    print("You drank something")

def study():
    time.sleep(5)
    print("You studied")

x = threading.Thread(target=eat, args=())
x.start()

y = threading.Thread(target=drink, args=())
y.start()

z = threading.Thread(target=study, args=())
z.start()

x.join()  # A função join faz com que o thread espeficicado sincronize com a main, assim o main thread só completara sua função quando um thread especifico completar sua função.

#eat()
#drink()
#study()

print(threading.active_count())
print(threading.enumerate())
print(time.perf_counter())
"""

# FIM #

# Daemon threads #  = um thread que roda em background, nao e importante para a execução do programa
#                     seu programa nao ira esperar pelo daemon threads para completar antes de sair
#                     non-daemon threads nao podem ser normamelmente "mortos", ficam "vivos" até sua execução completar
#                     O programa que esta sendo executado em uma daemon thread só "morrera" quando a função main concluir seu papel
"""
import threading
import time

def timer():
    print()
    print()
    count = 0
    while True:
        time.sleep(1)
        count += 1
        print("Logged in for : ", count, "seconds")

x = threading.Thread(target=timer, daemon= True)
x.start()

print(x. isDaemon())

answer = input("Do you wish to exit ?")

"""

# FIM #

# Multiprocessing # : rodar tarefar em paralelo em diferentes nucleos do cpu
#                     multiprocessamento : melhor para tarefas vinculadas ao processador (alto uso de cpu)
#                     multithreading : melhor para tarefas vinculadas a io (otimizada a espera de respostas)

# obs : por algum motivo que desconheco nao deu certo
"""
from multiprocessing import Process, cpu_count
import time

def counter(num):
    count = 0
    while count < num:
        count += 1

def main():
    a = Process(target=counter, args=(25000000,))
    b = Process(target=counter, args=(25000000,))
    c = Process(target=counter, args=(25000000,))
    d = Process(target=counter, args=(25000000,))

    a.start() 
    b.start() 
    c.start() 
    d.start() 

    a.join()
    b.join()
    c.join()
    d.join()

    print("Finished in : ", time.perf_counter(), "seconds")

if __name__ == "__main__":
    main()
"""

# FIM #

# Gui Windows #

# Widgets : GUI elements : buttons, textboxes, labels, images
# windows : serves as a container to hold or contain these widgets

"""
from tkinter import *

window = Tk() #Fundamenta a instancia de uma janela
window.geometry("420x420") #Define a resolução da janela
window.title("Testando") #Define o nome da janela

icon = PhotoImage(file="Banner.png") #Define o arquivo parxa ser usado como icone
window.iconphoto(True,icon) #Para inserir alguma foto como icone, precisa tranformala em "photoimage"
window.config(background="pink") #Define a cor de fundo

window.mainloop() #Coloca uma janela na tela do computador , espera por eventos
"""

# FIM #

# Labels # : é a area de um widget que armazena texto e/ou uma imagem dentro de uma janela
# fg = cor do texto
# bg = cor de fundo
# relief = borda customizada
# bd = tamanho da borda 
# padx = distancia entre a borda das letras no eixo x
# pody = disatncia entre a borda das letras no eixo y
# image = define uma imagem
# compund = define onde a imagem aparecera

"""
from tkinter import *

window = Tk( )

photo = PhotoImage(file=('C:\\Users\\Artu\\Desktop\\Banner.png')) #Inserindo a foto na pasta do programa tambem funciona

#label = Label(window,text="Hello world") #Criando o label
label = Label(window,text="Hello World !",font=('Arial',40,'bold'), fg='green', bg=('black'), relief=(RAISED), bd =30, padx=20, pady=20, image= photo, compound='bottom') #Texto com customizacoes 
label.pack() #Aloca o label na janela, porpadrao se alinha ao centro
#label.place(x=0,y=0) Define onde o texto vai aparecer por coordenadas

window.mainloop()
"""

# FIM # 

# Buttons # 

# activeforeground = cor do botao ativo
# activebackground = cor de fundo ao clicar

'''
from tkinter import *

count = 0

window = Tk()

def click():
    global count
    count+=1
    print(count)

photo = PhotoImage(file='like.png')

button = Button(window,
                text = "Click me", 
                command=click,
                font=("Comic Sans",30),
                fg="green",
                bg="black",
                activeforeground="green", 
                activebackground="pink", #Cor de fundo ao clicar no botao
                state=ACTIVE, #DISABLED = desativa o botao
                image=photo,
                compound='bottom') 
button.pack()

window.mainloop()
'''

# FIM #

# Entrybox #

'''
from tkinter import *
 
# Entry widget : textbox that accepts a single line of user input

window = Tk()

entry = Entry(window,font=("TimesNewRoman",50))
entry.pack()
 
window.mainloop() 
 
 '''

for i,x in enumerate(['A','B','C']):
    print(i,x)