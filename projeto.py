import  sys

TODO_FILE = 'todo.txt'
ARCHIVE_FILE = 'done.txt'

RED   = "\033[1;31m"  
BLUE  = "\033[0;34m"
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

      if len(tokens) > 1 and contextoValido(tokens[-2])== True:
         contex = tokens[-2]
         tokens.pop(-2)
         
      if projetoValido(tokens[-1])== True:
         proj = tokens[-1]
         tokens.pop(-1)
         
      for x in tokens:
         desc += x +' '
         
   itens.append((desc,(data, hora, pri, contex, proj)))
   return itens

def organizadoBonito(bagunca):
   novaOrdem = []
   junto= ''
   espaço =' '
  
   if bagunca[0][1][0] != '':
      dataNaOrdem = dataBonita(bagunca[0][1][0])
      junto+= dataNaOrdem +espaço
      
   if bagunca[0][1][1] != '':
      horaNaOrdem = horaBonita(bagunca[0][1][1])
      junto+= horaNaOrdem +espaço
      
   if bagunca[0][1][2] != '':
      priNaOrdem = bagunca[0][1][2]
      junto+= priNaOrdem +espaço
      
   if bagunca [0][0] != '':  
      descNaOrdem = bagunca[0][0]
      junto+= descNaOrdem +espaço

   if bagunca[0][1][3] != '':
      contxtNaOrdem = bagunca[0][1][3]
      junto+= contxtNaOrdem +espaço

   if bagunca[0][1][4] != '': 
      projNaOrdem = bagunca[0][1][4] 
      junto+= projNaOrdem +espaço

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
            if itens[x][0][1][0] > itens[x+1][0][1][0] and itens[x][0][1][0] is not  '':
               itens[x],itens[x+1] = itens[x+1] , itens[x]
            if itens[x][0][1][0] == itens[x+1][0][1][0]:
              if itens[x][0][1][1] > itens[x+1][0][1][1] and itens[x+1][0][1][1] is not '' or itens[x][0][1][1] < itens[x+1][0][1][1] and itens[x][0][1][1] is  '':
                 itens[x],itens[x+1] = itens[x+1],itens[x]
            
            if itens[x][0][1][0] < itens[x+1][0][1][0] and itens[x][0][1][0] is  '':
               itens[x],itens[x+1] = itens[x+1] , itens[x]
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
      cont+=1      
   for x in range(qteDeAtividade):      
      if itens[x][0][1][2] == vazio:
         itens2.append(itens[x])       
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
  linhasDoArquivo = abrir()
  listagem = listar()
  atividadeRealizada = organizadoBonito(listagem[num])
  qte = len(linhasDoArquivo)
  cont = 0
  while cont < qte:
    pivo = linhasDoArquivo[cont]
    pivo = organizadoBonito(organizar(pivo))
    if pivo[:-2] == atividadeRealizada[:-2]:
      adicionaFeito(pivo)
      linhasDoArquivo.pop(cont)
      qte-=1
    cont +=1
    
  print('{}foi feito'.format(atividadeRealizada))
  return reescrever(linhasDoArquivo)


def remover(x):
  linhasDoArquivo = abrir()
  listagem = listar()
  item = organizadoBonito(listagem[x])
  qte = len(linhasDoArquivo)
  cont = 0
  while cont < qte:
    pivo = linhasDoArquivo[cont]
    pivo = organizadoBonito(organizar(pivo))
    if pivo[:-2] == item[:-2]:
      linhasDoArquivo.pop(cont)
      qte-=1
    cont +=1
  print('{}foi removido'.format(item))

  return reescrever(linhasDoArquivo)

def frases(elem,elem2):
  desc = elem
  data = elem2[0]
  hora = elem2[1]
  pri = elem2[2]
  ctx =elem2[3]
  proj =elem2[4]
  novaFrase=''
  espaço =' '
  if data is not '':
    novaFrase +=data+espaço
  if hora is not '':
    novaFrase +=hora+espaço
  if pri is not '':
    novaFrase+=pri+espaço
  if desc is not '':
    novaFrase+=desc+espaço
  if ctx is not '':
    novaFrase+=ctx+espaço
  if proj is not '':
    novaFrase+=proj
  return novaFrase +'\n'

def priorizar(num, prioridade):
  alterado = []
  atualizado =[]
  prioridade = '('+prioridade+') '
  linhasDoArquivo = abrir()
  a = listar()
  for x in range(len(a)):
    alterado.append(a[x][0])
  novadesc =alterado[num][0]
  data = alterado[num][1][0]
  hora = alterado[num][1][1]
  contexto = alterado[num][1][3]
  projeto = alterado[num][1][4]
  novaAtiv = (novadesc, (data, hora, prioridade, contexto, projeto))
  alterado.pop(num)
  alterado.insert(num,novaAtiv)
  for x in range(len(alterado)):
    novosItens = frases(alterado[x][0],alterado[x][1])
    atualizado.append(novosItens)
  print('Prioridade Alterada')

  return reescrever(atualizado)

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
        ordem = x+1
        espaço = ' '
        tarefa = str(ordem)+espaço+organizadoBonito(a[x])
        if a[x][0][1][2] == '(A)':
           printCores(tarefa,CYAN)
        elif a[x][0][1][2] == '(B)':
           printCores(tarefa,GREEN)
        elif a[x][0][1][2] == '(C)':
           printCores(tarefa,YELLOW)
        elif a[x][0][1][2] == '(D)' :
           printCores(tarefa,BLUE)
        else:
           print('{}'.format(tarefa)) 
      

  elif comandos[1] == REMOVER:
    atividade = comandos[2]
    atividade = int(atividade)
    if atividade not in range(len(listar)):
      print('A atividade indicada não existe')
    
    return remover(atividade-1)    

  elif comandos[1] == FAZER:
    colocacao = comandos[2]
    colocacao = int(colocacao)
    if colocacao not in range(len(listar())):
      print('A atividade indica não existe')
      return False
    else:
      return fazer(colocacao-1)    


  elif comandos[1] == PRIORIZAR:
    alfa ='QWERTYUIOPASDFGHJKLÇZXCVBNM'
    ordem = comandos[2]
    ordem = int(ordem)
    prioridade = comandos[3].upper()
    if prioridade not in alfa or ordem not in range(len(listar())):
      print('A atividade indica não existe')
      return False
    else:
      return priorizar(ordem-1,prioridade)

  else :
    print("Comando inválido.")
    
processarComandos(sys.argv)
