from Conversion import StringToBinary

with open('assembly.txt', 'r') as assemblyCode:
    assemblyLines = assemblyCode.readlines()

OPCodes = {
    'LOAD': '00000001', 'Loadnegative': '00000010', 'Loadabs': '00000011', 'ADD': '00000100',
    'ADDabs': '00000101', 'SUB': '00000110', 'SUBabs': '00000111', 'DIV': '00001000',
    'JUMPleft': '00001001', 'JUMPright': '00001010', 'JUMPcondleft': '00001011',
    'JUMPcondright': '00001111', 'LSH': '00010000', 'RSH': '00010001', 'STOR': '00010010',
    'FACT': '00010011', 'PERM': '00100100', 'LOAD MQ': '00100101'
}

assemblysplit = [i.split(' ') for i in assemblyLines]

start = assemblysplit.index(['\n']) + 1
# Converting the obtained data from the assembly code into readable data.

for i in range(start, len(assemblysplit)):
    assemblysplit[i][1] = assemblysplit[i][1].replace("M[", "")
    assemblysplit[i][1] = assemblysplit[i][1].replace("]", "")
    assemblysplit[i][1] = assemblysplit[i][1].replace(";", "")
    assemblysplit[i][1] = assemblysplit[i][1].replace("\n", "")
    if (len(assemblysplit[i]) > 2):
        assemblysplit[i][3] = assemblysplit[i][3].replace("M[", "")
        assemblysplit[i][3] = assemblysplit[i][3].replace("]", "")
        assemblysplit[i][3] = assemblysplit[i][3].replace(";", "")
        assemblysplit[i][3] = assemblysplit[i][3].replace("\n", "")
        assemblysplit[i][1] = assemblysplit[i][1].replace(",", "")


for i in range(start, len(assemblysplit)):
    if (assemblysplit[i][1] == "MQ"):
        assemblysplit[i][0] = "LOAD MQ"
        assemblysplit[i][1] = " "


Lines = []

# Converting the assembly code into machine code of 20 bits * 2 (8 bits opcode + 12 bit address)

for i in range(start, len(assemblysplit)):
    tmpcode = ''
    tmpcode += OPCodes[assemblysplit[i][0]]

    if (assemblysplit[i][1]).isnumeric():
        tmpcode += format(int(assemblysplit[i][1]), "012b")
    else:
        tmpcode += " " * 12

    if (len(assemblysplit[i]) > 2):
        tmpcode += OPCodes[assemblysplit[i][2]]
        if (assemblysplit[i][1]).isnumeric():
            tmpcode += format(int(assemblysplit[i][3]), "012b")
        else:
            tmpcode += " " * 12

    Lines.append(tmpcode)

for index, line in enumerate(Lines):
    if len(line) < 21:
        Lines[index] = line + " " * 20 + "\n"
    else:
        Lines[index] = line + "\n"


# Writing the produced Machine Code into a txt file

with open('machinecode.txt', 'w') as machineCODE:
    for line in Lines:
        machineCODE.write(line)
