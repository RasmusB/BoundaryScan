#! python3

import shlex
import collections

class TapUnit:
    def __init__(self):
        self.entity = ''
        self.physicalPinMap = ''
        self.ports = []
        self.pinMap = {}
        # Not sure what to to with this information
        # Populate with pin(s) and their required state
        self.compliancePattern = []
        self.irLength = 0
        self.instructions = []
        self.irCaptureValue = ''
        self.idCode = None
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
inputFile = './test_data/STM32F1_Med_density_LQFP48.bsd'
tapInstance = TapUnit()

# Parsing data helpers
nestingLevel = []
subsetOf = []

print(list(shlex.shlex(open(inputFile))))

inputData = (openAndCleanFile(inputFile))

for index, line in enumerate(inputData):
    lineDict = collections.defaultdict(int)

    for char in line :
        lineDict[char] += 1

    if index != 0:
        nestingLevel.append(lineDict['('] - lineDict[')'] + nestingLevel[index - 1])
    else:
        nestingLevel.append(lineDict['('] - lineDict[')'])

    if nestingLevel[index] == 0:
        keyword = line.split()[0]
        if keyword == 'entity':
            tapInstance.entity = line.split()[1]
            print(line.split())