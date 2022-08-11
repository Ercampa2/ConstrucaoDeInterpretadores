#Enzo Ramon Campa
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
