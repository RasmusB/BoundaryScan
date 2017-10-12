#! python3

import collections

class TapUnit:
    def __init__(self):
        self.name = ''
        self.package = ''
        self.ports = []
        self.pinMap = {}
        # Not sure what to to with this information
        # Populate with pin(s) and their required state
        self.compliancePattern = []
        self.irLength = 0
        self.instructions = []
        self.irCaptureValue = ''
        self.idCode = IDcode()
        self.regAccess = ''
        self.boundaryLength = 0
        self.boundaryRegister = []
        self.designWarning = ''

    class Port:
        def __init__(self, name, type, width):
            self.name = name
            self.type = type
            self.width = width

    class Instruction:
        def __init__(self, name, opcode):
            self.name = name
            self.opcode = opcode

    class IDcode:
        def __init__(self):
            self.version = ''
            self.partNo = ''
            self.manufacturer = ''

    class BoundaryCell:
        def __init__(self, num, cell, port, function, safe, ccell=None, disval=None, rslt=None):
            self.num = num
            self.cell = cell
            self.port = port
            self.function = function
            self.safe = safe
            self.ccell = ccell
            self.disval = disval
            self.rslt = rslt

def openAndCleanFile(filename) :

    fileContents = []
    noWhiteSpace = []
    noCommentLines = []
    noInlineComments = []
    codeLines = []
    finishedLines = []

    with open(filename) as inputFile :
        fileContents = list(inputFile)

    # Remove all leading/trailing whitespace, empty lines and line brakes
    for line in fileContents :
        temp = line.lstrip()
        temp = temp.rstrip()
        if temp != '' :
            noWhiteSpace.append(temp)

    # Remove all lines starting with a comment
    for line in noWhiteSpace :
        if line[0:2] != '--' :
            noCommentLines.append(line)

    # Remove all inline comments
    for line in noCommentLines :
        if '--' not in line :
            noInlineComments.append(line)
        else :
            temp = line.split('--')
            noInlineComments.append(temp[0])

    # Join broken lines into single lines
    tempLine = ''

    for line in noInlineComments:
        if ';' in line:
            if tempLine == '':
                tempLine = line
            else:
                tempLine = tempLine + ' ' + line
            codeLines.append(tempLine)
            tempLine = ''
        else :
            tempLine = tempLine + ' ' + line

    for line in codeLines:
        temp = line.replace('\t', ' ')
        temp = temp.split()
        temp = ' '.join(temp)
        temp = temp.strip()
        finishedLines.append(temp)

    return finishedLines

# Main program here
entityIndex = []
nestingLevelDiff = []

inputData = (openAndCleanFile('./test_data/STM32F1_Med_density_LQFP48.bsd'))

for index, line in enumerate(inputData):
    keyword = line.split()[0]
    lineDict = collections.defaultdict(int)

    print('Parsing line ' + str(index) + ': ' + line)

    for char in line :
        lineDict[char] += 1

    nestingLevelDiff.append(lineDict['('] - lineDict[')'])

