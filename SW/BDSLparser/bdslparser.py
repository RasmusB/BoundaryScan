#! python3

class TapUnit :
    def __init__(self):
        self.package = ''
        self.ports = []
        self.pinMap = {}
        # Not sure what to to with this information
        # Populate with pin(s) and their required state
        self.compliancePattern = []
        self.irLength = 0
        self.instructions = []
        self.irCaptureValue = ''
        self.idCode =



    class Port :
        def __init__(self, name, type, width):
            self.name = name
            self.type = type
            self.width = width

    class Instruction :
        def __init__(self, name, opcode):
            self.name = name
            self.opcode = opcode

    class IDcode :
        def __init__(self, version, partNo, manufacturer):
            self.version = version
            self.partNo = partNo
            self.manufacturer = manufacturer



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

    for line in noInlineComments :
        if ';' in line:
            tempLine = tempLine + line
            codeLines.append(tempLine)
            tempLine = ''
        else :
            tempLine = tempLine + ' ' + line

    for line in codeLines :
        temp = line.replace('\t', ' ')
        temp = temp.split('&')
        temp = ' '.join(temp)
        temp = temp.split()
        temp = ' '.join(temp)
        temp = temp.strip()
        finishedLines.append(temp)

    return finishedLines



inputData = (openAndCleanFile('./test_data/STM32F1_Med_density_LQFP48.bsd'))
for line in inputData :
    print(line)
