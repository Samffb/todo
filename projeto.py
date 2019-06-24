import  sys
#from datetime import date

TODO_FILE = 'testeProjetoAgenda.txt'
ARCHIVE_FILE = 'feito.txt'

RED   = "\033[1;31m"  
BLUE  = "\033[1;34m"
CYAN  = "\033[1;36m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
BOLD    = "\033[;1m"
REVERSE = "\033[;7m"
YELLOW = "\033[0;33m"

ADICIONAR = 'a'
REMOVER = 'r'
FAZER = 'f'
PRIORIZAR = 'p'
LISTAR = 'l'


def printCores(texto, cor) :
  print(cor + texto + RESET)

def adicionar(descricao,extras):
   
   #print(descricao)
   #print(extras)
   
  # não é possível adicionar uma atividade que não possui descrição.
  
   if descricao  == '' :
      return False
   
   espaço =' '
   vazio =''
   novaAtividade =''
   
   for x in range(0,3):
      if extras[x] is not '':
         novaAtividade += extras[x]+espaço
      
   novaAtividade += descricao + espaço
   
   for x in range(3,5):
      if extras[x] is not '':
         novaAtividade += extras[x]+espaço

   #if extras[0] == extras[1]== extras[2] == extras[3] == extras[4] == vazio:
      #novaAtividade = descricao
      
   print('Atividade Salva: {}'.format(novaAtividade))
  # Escreve no TODO_FILE. 
   try: 
      fp = open(TODO_FILE, 'a')
      fp.write(novaAtividade + "\n")
      fp.close()
   except IOError as err:
      print("Não foi possível escrever para o arquivo " + TODO_FILE)
      print(err)
      return False

   return True
 
def horaValida(hora):
   checagem = soDigitos(hora)
   
   if len(hora) != 4 or checagem == False :
      return False
   else:
      horas = int(hora[0:2])
      minutos = int(hora[2:5])
      if horas in range(0,24) and minutos in range(0,60):
         return True
      return False
   
def dataValida(data):
   check = soDigitos(data)
   
   if len(data)!= 8 or check == False:
      return False
   else:
      dia = int(data[0:2])
      mes = int(data[2:4])
      ano = int(data[4:9])
      if mes  not in range(1,13):
         return False
      
      if mes == 2:
         if dia in range(1,30):
            return True
         return False
      if mes ==1==3==5==7==8==10==12:
         if dia in range(1,32):
            return True
         return False
      else:
         if dia in range(1,31):
            return True
         return False
   
def projetoValido(proj):
   if len(proj)< 2 or proj[0] != '+':
      return False
   return True

def contextoValido(contex):
   if len(contex)< 2 or contex[0] != '@':
      return False
   return True
   
def prioridadeValida(pri):
   alfa = 'abcdefghojklmnopqrtuvwxyzABCDEFGHIJKLMNOPQRTUVWXYZ'
   aux = '()'
   if len(pri) == 3 and pri[0] in aux and pri[1] in alfa and pri[2] in aux :
      return True
   return False

   
#itens = [] 
def organizar(linhas):
   itens = []
   for l in linhas:
      data = ''
      hora = ''
      pri = ''
      desc = ''
      proj = ''
      contex = ''
      l = linhas.strip()
      tokens = l.split()

      if dataValida(tokens[0])== True:
         data = tokens[0]
         tokens.pop(0)
         
      if horaValida(tokens[0])== True:
         hora = tokens[0]
         tokens.pop(0)

      if prioridadeValida(tokens[0]) == True:
         pri = tokens[0]
         tokens.pop(0)

      if contextoValido(tokens[-2])== True:
         contex = tokens[-2]
         tokens.pop(-2)
         
      if projetoValido(tokens[-1])== True:
         proj = tokens[-1]
         tokens.pop(-1)
         
      for x in tokens:
         desc += x +' '
         
   itens.append((desc,(data, hora, pri, contex, proj)))
   #print(itens)
   return itens



def organizadoBonito(bagunca):
   novaOrdem = []
   junto= ''
   espaço =' '
   #semEspaço = bagunça.strip()
   #quebrado = semEspaço.split()
   
   # data hora prioridade desc @ +

   if bagunca[0][1][0] != '':
      dataNaOrdem = dataBonita(bagunca[0][1][0])
      #novaOrdem.insert(1,dataNaOrdem)
      #dataNaOrdem = bagunca[0][1][0]
      #novaOrdem.append(dataNaOrdem)
      junto+= dataNaOrdem +espaço
      
   if bagunca[0][1][1] != '':
      horaNaOrdem = horaBonita(bagunca[0][1][1])
      #novaOrdem.insert(2,horaNaOrdem)
      #horaNaOrdem = bagunca[0][1][1] 
      #novaOrdem.append(horaNaOrdem)
      junto+= horaNaOrdem +espaço
      
   if bagunca[0][1][2] != '':
      priNaOrdem = bagunca[0][1][2]
      #novaOrdem.insert(3,)
      #novaOrdem.append(priNaOrdem)
      junto+= priNaOrdem +espaço
      
   if bagunca [0][0] != '':  
      descNaOrdem = bagunca[0][0]
      #novaOrdem.insert(0,descNaOrdem)
      #novaOrdem.append(descNaOrdem)
      junto+= descNaOrdem +espaço

   if bagunca[0][1][3] != '':
      contxtNaOrdem = bagunca[0][1][3]
      #novaOrdem.append(contxtNaOrdem)
      junto+= contxtNaOrdem +espaço

   if bagunca[0][1][4] != '': #x
      projNaOrdem = bagunca[0][1][4] #x
      #novaOrdem.append(projNaOrdem) #x
      junto+= projNaOrdem +espaço
      
   #novaOrdem.append(junto)

   return junto



def dataBonita(data):
   dia = data[0:2] + '/'
   mes = data[2:4] + '/'
   ano = data[4:9]
   dataNova = dia+mes+ano
   return dataNova

def horaBonita(hora):
   h = hora[0:2] + 'h'
   m = hora[2:4] + 'm'
   horaNova = h+m
   return horaNova

   
def soDigitos(numero) :
  if type(numero) != str :
    return False
  for x in numero :
    if x < '0' or x > '9' :
      return False
  return True


def listar():
   organizacao= []
   arquivo= open(TODO_FILE,'r')
   todasAsLinhas = arquivo.readlines()
   arquivo.close()
   tamanho = len(todasAsLinhas)
   for i in range(tamanho):
      tarefa = organizar(todasAsLinhas[i])
      organizacao.append(tarefa)
   porPrioridade = ordenarPorPrioridade(organizacao)
   tudoOrdenado = ordenarPorDataHora(porPrioridade)
      
   
   return tudoOrdenado

def ordenarPorDataHora(itens):
   qte = len(itens)-1
   cont = 26
   while cont != 0 :
      for x in range(qte):
         if itens[x][0][1][2] ==  itens[x+1][0][1][2]:
            if itens[x][0][1][0] < itens[x+1][0][1][0]:
               itens[x],itens[x+1] = itens[x+1] , itens[x]
            if itens[x][0][1][0] == itens[x+1][0][1][0]:
              if itens[x][0][1][1] < itens[x+1][0][1][1]:
                 itens[x],itens[x+1] = itens[x+1],itens[x]
      cont -=1        
               
   return itens

def ordenarPorPrioridade(itens):
   qteDeAtividade = len(itens)
   vazio = ''
   itens2=[]
   alfa =('(A)','(B)','(C)','(D)','(E)','(F)','(G)','(H)','(I)','(J)','(K)','(L)','(M)','(N)','(O)','(P)','(Q)','(R)','(S)','(T)','(U)','(V)','(W)','(X)','(Y)','(Z)')
   cont = 0
   
   while cont != len(alfa):
      for x in range(qteDeAtividade):      
         if itens[x][0][1][2] == alfa[cont]:
            itens2.append(itens[x])
            #itens2.insert(x,itens[x])
      cont+=1      
   for x in range(qteDeAtividade):      
      if itens[x][0][1][2] == vazio:
         itens2.append(itens[x])
         #itens2.insert(-1,itens[x])
         
   itens = itens2
      
   return itens

def abrir():
  agenda =open(TODO_FILE,'r')
  todasAsLinhas = agenda.readlines()
  agenda.close
  return todasAsLinhas
  
def reescrever(linhasParaEscrever):
  qte = len(linhasParaEscrever)
  arquivo = open(TODO_FILE,'w')
  for x in range(qte):
    arquivo.write(linhasParaEscrever[x])
  arquivo.close()
  
def adicionaFeito(atividade):
  arquivoFeito = open(ARCHIVE_FILE,'a')
  arquivoFeito.write(atividade + ' \n')
  arquivoFeito.close()
  
  
def fazer(num):
  #agenda = open(TODO_FILE,'r')
  #todasAsLinhas = agenda.readlines()
  #agenda.close()
  linhasDoArquivo = abrir()
  listagem = listar()
  atividadeRealizada = organizadoBonito(listagem[num])
  qte = len(linhasDoArquivo)
  cont = 0
  while cont < qte:
    pivo = linhasDoArquivo[cont]
    pivo = organizadoBonito(organizar(pivo))
    if pivo[:-2] == atividadeRealizada[:-2]:
      #arquivoFeito = open(ARCHIVE_FILE,'a')
      #arquivoFeito.write(pivo + ' \n')
      #arquivoFeito.close()
      adicionaFeito(pivo)
      linhasDoArquivo.pop(cont)
      qte-=1
    cont +=1
    
  print('{}foi feito'.format(atividadeRealizada))
  #arquivo = open(TODO_FILE,'w')
  #for x in range(qte):
    #arquivo.write(todasAsLinhas[x])
  #arquivo.close()

  return reescrever(linhasDoArquivo)


def remover(x):
  #agenda =open(TODO_FILE,'r')
  #todasAsLinhas = agenda.readlines()
  #agenda.close
  linhasDoArquivo = abrir()
  listagem = listar()
  #print(listagem)
  #print('\n')
  item = organizadoBonito(listagem[x])
  #print(item)
  ##print('\n')
  #print(todasAsLinhas)
  qte = len(linhasDoArquivo)
  cont = 0
  while cont < qte:
    pivo = linhasDoArquivo[cont]
    pivo = organizadoBonito(organizar(pivo))
    if pivo[:-2] == item[:-2]:
      linhasDoArquivo.pop(cont)
      qte-=1
    cont +=1
  #print(todasAsLinhas)
  print('{}foi removido'.format(item))

  return reescrever(linhasDoArquivo)
  
  #arquivo = open(TODO_FILE,'w')
  
  #for x in range(qte):
    #arquivo.write(todasAsLinhas[x])
  #arquivo.close()
  
  #return todasAsLinhas


# prioridade é uma letra entre A a Z, onde A é a mais alta e Z a mais baixa.
# num é o número da atividade cuja prioridade se planeja modificar, conforme
# exibido pelo comando 'l'.
'''
def paraPriorizar(corpo,adicional,prioridade):
  espaço =' '
  vazio =''
  comPrioridade =''
  adicional[2] = prioridade
   
  for x in range(0,3):
    if adicional[x] is not '':
      comPrioridade += adicional[x]+espaço
      
  comPrioridade += corpo + espaço
   
  for x in range(3,5):
    if adicional[x] is not '':
      comprioridade += adicional[x]+espaço

  return comPrioridade
  '''
      
def priorizar(num, prioridade):
  prioridade = '('+prioridade+') '
  linhasDoArquivo = abrir()
  listagem = listar()
  #print(listagem)
  atividadeRealizada = organizadoBonito(listagem[num])
  #print(atividadeRealizada)
  qte = len(linhasDoArquivo)
  cont = 0
  while cont < qte:
    pivo = linhasDoArquivo[cont]
    pivo = organizadoBonito(organizar(pivo))
    if pivo[:-2] == atividadeRealizada[:-2]:
      item = organizar(pivo)
      linhasDoArquivo.pop(cont)
      espaço = ' '
      corpo = item[0][0]
      vazio = ''
      comPri = ''
      #print('esse eh o item {}'.format(item))
      #print('este eh o corpo {}'.format(corpo))
      for i in range(0,2):
        if item[0][1][i] != vazio:
          add = item[0][1][i]
          comPri += add+ espaço
      comPri+= prioridade + corpo + espaço

      for x in range(3,5):
        if item[0][1][i] != vazio:
          add = item[0][1][i]
          comPri += add
      #adicionaFeito(comPri +'\n')
      #print('\n',comPri)
      linhasDoArquivo.append(comPri +'\n')
      #linhasDoArquivo.pop(cont)
      qte-=1
    cont +=1
  #print(linhasDoArquivo)
  return reescrever(linhasDoArquivo)







  '''
  
  print(todasAsAtividades)
  print(prioridade)
  listagem = listar()
  alterarPri = organizadoBonito(listagem[num])
  qte = len(todasAsAtividades)
  cont = 0
  while cont < qte:
    pivo = todasAsAtividades[cont]
    pivo = organizadoBonito(organizar(pivo))
    if pivo[:-2] == alterarPri[:-2]:
      
      #pivo = organizar(pivo)
      #print(pivo)
      #comPri = paraPriorizar(pivo[0][0],pivo[0][1],prioridade)
      #todasAsAtividades.pop(cont)
      #todasAsAtividades.append(comPri)
      #qte -=1
      
      arrumado = organizar(pivo)
      espaço =' '
      vazio =''
      comPrioridade =''
      #arrumado[0][1][2] = prioridade
      corpo = arrumado[0][0]
   
      for x in range(0,2):
        if arrumado[0][1][x] is not '':
          comPrioridade += arrumado[0][1][x]+espaço
          
      comPrioridade += corpo + espaço
       
      for x in range(3,5):
        if arrumado[x] is not '':
          comPrioridade += proridade+arrumado[x]+espaço
      todasAsAtividades.pop(cont)
      todasAsAtividades.append(comPri)
      qte -=1
          
  print('{}teve sua prioridade alterada.'.format(pivo))
  return reescrever(linhasDoArquivo)
  '''
      

  ################ COMPLETAR

  #return 




      
      


def processarComandos(comandos):
  if comandos[1] == ADICIONAR:
    comandos.pop(0)
    comandos.pop(0)
    itemParaAdicionar = organizar(' '.join(comandos))[0]
    adicionar(itemParaAdicionar[0],itemParaAdicionar[1])
      
  elif comandos[1] == LISTAR:  
    if listar() == []:
      return False
    else:
      a = listar()
      for x in range(len(a)):
        #if a[x][0][1][2] == '(A)':
          #print('{} {}'.format(x+1,printCores(organizadoBonito(a[x]),YELLOW)))
        #elif a[x][0][1][2] == '(B)':
          #print('{} {}'.format(x+1,printCores(organizadoBonito(a[x]),BLUE)))
        #elif a[x][0][1][2] == '(C)':
          #print('{} {}'.format(x+1,printCores(organizadoBonito(a[x]),CYAN)))
        #elif a[x][0][1][2] == '(D)':
          #print('{} {}'.format(x+1,printCores(organizadoBonito(a[x]),GREEN)))
        #else:
          print('{} {}'.format(x+1,organizadoBonito(a[x])))
   
    ################ COMPLETAR

  elif comandos[1] == REMOVER:
    atividade = comandos[2]
    atividade = int(atividade)
    
    return remover(atividade-1)    

  elif comandos[1] == FAZER:
    colocacao = comandos[2]
    colocacao = int(colocacao)
    
    return fazer(colocacao-1)    

    #return    

    ################ COMPLETAR

  elif comandos[1] == PRIORIZAR:
    alfa ='QWERTYUIOPASDFGHJKLÇZXCVBNM'
    ordem = comandos[2]
    ordem = int(ordem)
    prioridade = comandos[3].upper()
    if prioridade not in alfa:
      return False
    else:
      return priorizar(ordem-1,prioridade)
    

    ################ COMPLETAR

  else :
    print("Comando inválido.")
    
processarComandos(sys.argv)

   
