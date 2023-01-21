import string
# from pprint import pprint

ciente = "N"

lista = {}
listaRec = {}
listaFerias = {}
listaAlunos = {}

qtdAlunos = 0
id = 0
notaRecuperacao = 0.0

def mostrarAlunos():
  try:
    print()
    for x in range(len(lista)):
      y = lista["{}".format(x)]["nome"]
      print("({}:(nome:{}))".format(x,y))
    print()
    
  except:
    print()
    print("Ocorreu um erro")
    print()

def recebeAlunos():
    global qtdAlunos
    while qtdAlunos < 1 or qtdAlunos > 50:
        try:
            print("///////////////////////////////////////////////////////") 
            print("Por favor, insira a quantidade de alunos da sua turma ")            
            print("///////////////////////////////////////////////////////")
            qtdAlunos = int(input("=> ")) 
            if qtdAlunos < 10 or qtdAlunos > 50:
                print()
                print("Quantidade inválida!!!!!!!")
                print("Por favor, insira um número entre 10 e 50")
                print()
        except:
            print()
            print("Erro!!!!")
            print("Insira apenas números inteiros")
            print()
            
    try:
        for i in range(qtdAlunos):
            validos = string.ascii_letters + ' '
            while True:
                print("///////////////////////////////////////////////////////") 
                print("//////     Digite o nome do aluno {}       //////".format(i + 1))                
                print("///////////////////////////////////////////////////////") 
                addNome = input("=> ").lower().capitalize()
                print()
                if all(c in validos for c in addNome):
                    lista.update({"{}".format(i):{"nome":str(addNome)}})
                    break
                else:
                    print()
                    print("Erro!!!!")
                    print("Por favor digite um nome válido (somente letras e espaços)")
                    print()
            
    except:
        print("Houve um erro")

# def ordenaLista():
#     for i in range(len(lista)):
#         sortedList = sorted(lista, )
#         pprint(sortedList)


def insereNota1():
    for x in range(len(lista)):
        nome = lista["{}".format(x)]["nome"]
        nota1 = -1
        while nota1 < 0 or nota1 > 10:
            try:
                print("///////////////////////////////////////////////////////") 
                print("Insira a nota do(a) aluno(a) {} no primeiro trimestre ".format(nome))                
                print("///////////////////////////////////////////////////////") 
                nota1 = int(input("=> "))
                print()
                if nota1 < 0 or nota1 > 10:
                    print()
                    print("Quantidade inválida!")
                    print("Por favor, insira um número entre 0 e 10")
                    print()
                    
            except:
                print()
                print("Erro!!!!")
                print("Insira apenas números inteiros de 0 a 10")
                print()

        lista.update({"{}".format(x):{"nome":str(nome),"nota1":str(nota1)}})

def mostrarNota1():
    
    for x in range(len(lista)):
        nome =  lista["{}".format(x)]["nome"]
        nota1 =  lista["{}".format(x)]["nota1"]
        try:
            print()
            print("({}:(nome:{})(nota 1:{}))".format(x,nome,nota1))
            print()
        
        except:
            print()
            print("Ocorreu um erro")
            print()

def insereNota2():
    for x in range(len(lista)):
        nome = lista["{}".format(x)]["nome"]
        nota1 = lista["{}".format(x)]["nota1"]
        nota2 = -1
        while nota2 < 0 or nota2 > 10:
            try:
                print("///////////////////////////////////////////////////////") 
                print("Insira a nota do(a) aluno(a) {} no segundo trimestre ".format(nome))                
                print("///////////////////////////////////////////////////////") 
                nota2 = int(input("=> "))
                print()
                if nota2 < 0 or nota2 > 10:
                    print()
                    print("Quantidade inválida!")
                    print("Por favor, insira um número entre 0 e 10")
                    print()
                    
            except:
                print()
                print("Erro!!!!")
                print("Insira apenas números inteiros de 0 a 10")
                print()
        lista.update({"{}".format(x):{"nome":str(nome),"nota1":str(nota1), "nota2":str(nota2)}})
        

def mostrarNota2():
    for x in range(len(lista)):
        nome =  lista["{}".format(x)]["nome"]
        nota1 = lista["{}".format(x)]["nota1"]
        nota2 = lista["{}".format(x)]["nota2"]
        try:
            
            print()
            print("({}:(nome:{})(nota 1:{})(nota 2:{}))".format(x, nome, nota1, nota2))
            print()
        
        except:
            print()
            print("Ocorreu um erro")
            print()



def cacularMedia():
  for x in range(len(lista)):
    try:
        nome = lista["{}".format(x)]["nome"]
        nota1 = float(lista["{}".format(x)]["nota1"])
        nota2 = float(lista["{}".format(x)]["nota2"])
        media = (nota1 + nota2) / 2
        lista.update({"{}".format(x):{"nome":str(nome),"nota1":str(nota1),"nota2":str(nota2),"mediaParcial":(media)}})
    except:
        print()
        print("Ocorreu um erro")
        print()




def mostrarMedia():
    print("///////////////////////////////////////////////////////")
    print("/////               Notas parciais                /////")
    print("///////////////////////////////////////////////////////") 
    print()
    for x in range(len(lista)):
        nome = lista["{}".format(x)]["nome"]
        nota1 = lista["{}".format(x)]["nota1"]
        nota2 = lista["{}".format(x)]["nota2"]
        media = lista["{}".format(x)]["mediaParcial"]
        try:
            print("{} nome:{} nota 1:{} nota 2:{} media parcial:{})".format(x, nome, nota1, nota2, media))
            print()
        except:
            print()
            print("Ocorreu um erro")
            print()


def recuperacao():
    f = 0
    r = 0
    for x in range(len(lista)):
        nome = lista["{}".format(x)]["nome"]
        nota1 = lista["{}".format(x)]["nota1"]
        nota2 = lista["{}".format(x)]["nota2"]
        media = float(lista["{}".format(x)]["mediaParcial"])
        try:            
            if media >= 6:
                lista.update({"{}".format(x):{"nome":str(nome),"nota1":str(nota1),"nota2":str(nota2),"recuperacao":"Não","mediaFinal":str(media),"situacao":"Aprovado"}})
                listaFerias.update({"{}".format(f):{"nome":str(nome)}})
                f += 1
            elif media < 6:
                lista.update({"{}".format(x):{"nome":str(nome),"nota1":str(nota1),"nota2":str(nota2),"recuperacao":"Não","mediaFinal":str(media),"situacao":"Pendente"}})
                listaRec.update({"{}".format(r):{"id":str(x),"nome":str(nome)}})
                r += 1
        except:
            print()
            print("Ocorreu um erro")
            print()
    print("///////////////////////////////////////////////////////")
    print("//////        Alunos que estão de férias!        //////")
    print("///////////////////////////////////////////////////////")
    print()
    for x in range(len(listaFerias)):
        print(listaFerias["{}".format(x)]["nome"])
    print()
    print("///////////////////////////////////////////////////////")
    print("//////     Alunos que necessitam recuperação     //////")
    print("///////////////////////////////////////////////////////")
    print()
    for x in range(len(listaRec)):
        nome =  listaRec["{}".format(x)]["nome"] 
        id = listaRec["{}".format(x)]["id"]
        print(id," ",nome)
    confirmarCiencia()
    

def confirmarCiencia():
    global ciente
    print()
    print("///////////////////////////////////////////////////////////////////////")
    print("Confirma estar ciente sobre a situação de todos os alunos?('s' ou 'n') ")
    print("///////////////////////////////////////////////////////////////////////")
    ciente = input("=> ")
    print()
    
    if ciente == 's' or ciente == 'S':        
        for x in range(len(listaRec)):
            id = listaRec["{}".format(x)]["id"]
            nomeRec = listaRec["{}".format(x)]["nome"]
            print("///////////////////////////////////////////////////////")
            print("Insira a nota de recuperação do(a) aluno(a) {} ".format(nomeRec))
            print("///////////////////////////////////////////////////////")
            notaRec = int(input("=> "))
            print()
            listaRec.update({"{}".format(x):{"id":str(id),"nome":str(nomeRec),"notaRecuperacao":str(notaRec)}})
    elif ciente == 'n' or ciente == 'N':
        programa()
    else:
        print()
        print("Erro!!!!")
        print("Por favor, digite 'S' (para 'sim') ou 'N' (para 'nao') para prosseguir")
        print()
        confirmarCiencia()




def inserirMediaFinal():
    for y in range(len(listaRec)):
        global notaRecuperacao
        notaRec = listaRec["{}".format(y)]["notaRecuperacao"]
        id = listaRec["{}".format(y)]["id"]
        notaRecuperacao = float(notaRec)
    
        for x in range(len(lista)):
            nome = lista["{}".format(x)]["nome"]
            nota1 = float(lista["{}".format(x)]["nota1"])
            nota2 = float(lista["{}".format(x)]["nota2"])
            media = float(lista["{}".format(x)]["mediaFinal"])
            mediaFinal = (media + notaRecuperacao) / 2
            
            if mediaFinal >= 6:
                situacao = "Aprovado"
            elif mediaFinal < 6:
                situacao = "Reprovado"

            if media < 6 and id == str(x) :
                lista.update({"{}".format(x):{"nome":str(nome),"nota1":str(nota1),"nota2":str(nota2),"mediaFinal":str(mediaFinal),"recuperacao":str(notaRec),"situacao":str(situacao)}})


def mostrarResultado():
    print("///////////////////////////////////////////////////////")
    print("//////             Fim do Semestre!!             //////")
    print("//////                  BOLETIM                  //////")
    print("///////////////////////////////////////////////////////")
    print()
    for x in range(len(lista)):
        nome = lista["{}".format(x)]["nome"]
        nota1 = lista["{}".format(x)]["nota1"]
        nota2 = lista["{}".format(x)]["nota2"]
        recuperacao = lista["{}".format(x)]["recuperacao"]
        media = lista["{}".format(x)]["mediaFinal"]        
        situacao = lista["{}".format(x)]["situacao"]

        try:
            lista.update({"{}".format(x):{"nome":str(nome),"nota1":str(nota1),"nota2":str(nota2),"recuperacao":str(recuperacao),"mediaFinal":str(media),"situacao":str(situacao)}})
             
            print("({} nome: {} nota 1: {} nota 2: {} recuperacao: {} media final: {} situação: {})".format(x, nome, nota1, nota2, recuperacao, media, situacao))
            print()
        except:
            print()
            print("Ocorreu um erro")
            print()


def programa():    
    try:
        # ordenaLista()

        # mostrarAlunos()

        insereNota1()

        insereNota2()

        # mostrarNota1()

        # mostrarNota2()

        cacularMedia()

        mostrarMedia()

        recuperacao()

        inserirMediaFinal()

        mostrarResultado()
    except:
        print("Ocorreu um erro")

