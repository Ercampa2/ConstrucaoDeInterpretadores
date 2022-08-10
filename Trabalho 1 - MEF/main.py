#Parâmetros

alphabet = ['a', 'b', 'c']

txt = open("test03.txt", 'r')

#funções de estado

def State1(txt, index):
  if(len(txt) <= index):
    return printResult(txt, True)
  if(txt[index] == 'b' or txt[index] == 'c'):
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

#funções Utilitárias 

def printResult(txt, val):
  if(val):
    return print(txt,": Pertence", sep="")
  return print(txt,": Não pertence", sep="")

#body
  
lineCount = int(txt.readline())

for line in range(lineCount):
  text = txt.readline()
  text2 = text.rstrip('\n')
  State1(text2, 0)
  
txt.close()