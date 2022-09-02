#Enzo Ramon Campa

#Para  obter  os  pontos  relativos  a  este  trabalho,  você  deverá  fazer  um  programa,  usando  a 
#linguagem de programação que desejar, que seja capaz de validar expressões de lógica propisicional 
#escritas em latex e definir se são expressões gramaticalmente corretas. Você validará apenas a forma 
#da expressão (sintaxe).  
#A entrada será fornecida por um arquivo de textos que será carregado em linha de comando, 
#com a seguinte formatação:  
#1. Na primeira linha deste arquivo existe um número inteiro que informa quantas expressões 
#lógicas estão no arquivo.  
#2. Cada uma das linhas seguintes contém uma expressão lógica que deve ser validada.  
#A saída do seu programa será no terminal padrão do sistema e constituirá de uma linha de saída 
#para cada expressão lógica de entrada contendo ou a palavra valida ou a palavra inválida e nada mais. 
#Gramática:  
#Formula=Constante|Proposicao|FormulaUnaria|FormulaBinaria.  
#Constante="T"|"F". 
#Proposicao=[a−z0−9]+ 
#FormulaUnaria=AbreParen OperadorUnario Formula FechaParen 
#FormulaBinaria=AbreParen OperatorBinario Formula Formula FechaParen 
#AbreParen="(" 
#FechaParen=")" 
#OperatorUnario="¬" 
#OperatorBinario="∨"|"∧"|"→"|"↔" 
 
#Cada  expressão  lógica  avaliada  pode  ter  qualquer  combinação  das  operações  de  negação, 
#conjunção, disjunção, implicação e bi-implicação sem limites na combiação de preposições e operações. 
#Os valores lógicos True e False estão representados na gramática e, como tal, podem ser usados em 
#qualquer expressão de entrada. 

formula = ["Const", "Prop", "FormUn", "FormBin"]

currentFormula = []
parenCounter = 0


def nextChar(text, index):
    global parenCounter
    if (len(text) <= index):
        if (parenCounter != 0):
            return print("Inválido")

        for cfl in range(len(currentFormula)):

            if (currentFormula[cfl] == "Const"):
                continue

            if (currentFormula[cfl] == "Prop"):
                continue

            if (currentFormula[cfl] == "FormUn"
                    and len(currentFormula) > cfl + 1):
                if (currentFormula[cfl + 1] in formula):
                    continue

            if (currentFormula[cfl] == "FormBin"
                    and len(currentFormula) > cfl + 2):
                if (currentFormula[cfl + 1] in formula
                        and currentFormula[cfl + 2] in formula):
                    continue

            return print("Inválido")

        return print("Valido")

    if (text[index] == "("):

        index += 1
        parenCounter += 1

        if (text[index] == "\\"):
            operator = findOperator(text, index + 1)

            if (operator == "neg"):
                currentFormula.append("FormUn")

            elif (operator == "wedge"):
                currentFormula.append("FormBin")

            elif (operator == "vee"):
                currentFormula.append("FormBin")

            elif (operator == "rightarrow"):
                currentFormula.append("FormBin")

            elif (operator == "leftrightarrow"):
                currentFormula.append("FormBin")

            else:
                return print("Invalido")
            nextChar(text, index + len(operator) + 1)

        else:
            return print("inválido")

    elif ((text[index].isalpha() or text[index].isnumeric()
           or text[index] == "T" or text[index] == "F")
          and text[index - 1] == " "):
        currentFormula.append("Prop")
        nextChar(text, index + 1)

    elif (text[index] == "T" or text[index] == "F"):
        currentFormula.append("Const")
        nextChar(text, index + 1)

    elif ((text[index].isalpha() or text[index].isnumeric()) and index == 0
          and text[index].islower()):
        currentFormula.append("Prop")
        nextChar(text, index + 1)

    elif ((text[index].isalpha() or text[index].isnumeric())
          and text[index].islower()):
        nextChar(text, index + 1)

    elif (text[index] == " "):
        nextChar(text, index + 1)

    elif (text[index] == ")"):
        parenCounter -= 1
        nextChar(text, index + 1)

    else:
        print("Invalido")


def findOperator(text, index):
    if (len(text) == index):
        return ""

    if (text[index].isalpha()):
        return text[index] + findOperator(text, index + 1)

    return ""


def fileReader(text):
    global parenCounter
    lineCount = int(text.readline())

    for x in range(lineCount):
        currentFormula.clear()
        parenCounter = 0
        textLine = text.readline()
        textNoBreak = textLine.rstrip('\n')

        nextChar(textNoBreak, 0)
    text.close()


txt1 = open("test01.txt", 'r')
txt2 = open("test02.txt", 'r')
txt3 = open("test03.txt", 'r')

fileReader(txt1)
fileReader(txt2)
fileReader(txt3)
