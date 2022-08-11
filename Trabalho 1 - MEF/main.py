#Enzo Ramon Campa

#Para  obter  os  pontos  relativos  a  este  trabalho,  você  deverá  criar  um  programa,  utilizando  a 
#linguagem  Python, C, ou C++.  Este  programa,  quando  executado,  irá  determinar  se  uma  string de 
#entrada  faz  parte  da  linguagem  𝐿    definida  por  𝐿 = {𝑥 | 𝑥 ∈
# {𝑎,𝑏}∗ 𝑒 𝑐𝑎𝑑𝑎 𝑎 𝑒𝑚 𝑥 é 𝑠𝑒𝑔𝑢𝑖𝑑𝑜 𝑝𝑜𝑟 𝑝𝑒𝑙𝑜 𝑚𝑒𝑛𝑜𝑠 𝑑𝑜𝑖𝑠 𝑏} segundo o alfabeto  Σ={𝑎,𝑏,𝑐}.  
#O  programa  que  você  desenvolverá  irá  receber  como  entrada um arquivo de texto  (.txt) 
#contendo várias strings. A primeira linha do arquivo indica quantas strings estão no arquivo de texto de 
#entrada. As linhas subsequentes contém uma string por linha.  A seguir está um exemplo das linhas que 
#podem existir em um arquivo de testes para o programa que você irá desenvolver: 
#3 
#abbaba 
#abababb 
#bbabbaaab 
#Neste  exemplo  temos  3  strings  de  entrada.  O  número  de  strings em  cada  arquivo  será 
#representado  por  um  número  inteiro  positivo.  A  resposta  do  seu  programa  deverá  conter  uma, e 
#somente uma linha de saída para cada string. Estas linhas conterão a string de entrada e o resultado 
#da validação conforme o formato indicado a seguir: 
#abbaba: não pertence.   
#A  saída  poderá  ser  enviada  para  um  arquivo  de  textos,  ou  para  o  terminal  padrão  e  será 
#composta de uma linha de saída por string de entrada. No caso do exemplo, teremos 3 linhas de saída. 
#Para que seu programa possa ser testado você deve criar, no mínimo, três arquivos de entrada 
#contendo um número diferente de strings diferentes. Os arquivos de entrada criados para os seus testes 
#devem estar disponíveis tanto no ambiente repl.it quanto no ambiente Github. Observe que o professor 
#irá  testar  seu  programa  com  os  arquivos  de  testes  que  você  criar  e  com,  no  mínimo  um  arquivo  de 
#testes criado pelo próprio professor.  

#---Funções de estado---

def State1(txt, index):
  if(len(txt) <= index):
    return printResult(txt, True)
  if(txt[index] == 'b'):
    return State1(txt, index+1)
  if(txt[index] == 'a'):
    return State2(txt, index+1)  
  return State4(txt)
  
def State2(txt, index):
  if(len(txt) <= index):
    return State4(txt)
  if(txt[index] == 'b'):
    return State3(txt, index+1)
  return State4(txt)  

def State3(txt, index):
  if(len(txt) <= index):
    return State4(txt)
  if(txt[index] == 'b'):
    return State1(txt, index+1)
  return State4(txt)

def State4(txt):
  return printResult(txt, False)

#---funções Utilitárias---

def printResult(txt, val):
  if(val):
    return print(txt,": Pertence.", sep="")
  return print(txt,": Não pertence.", sep="")

def fileReader(text):
  lineCount = int(text.readline())

  for x in range(lineCount):
    textLine = text.readline()
    textNoBreak = textLine.rstrip('\n')
    State1(textNoBreak, 0)
  text.close()

#---Parâmetros---

txt1 = open("test01.txt", 'r')
txt2 = open("test02.txt", 'r')
txt3 = open("test03.txt", 'r')

#---Chamada das funções---

fileReader(txt1)
fileReader(txt2)
fileReader(txt3)
