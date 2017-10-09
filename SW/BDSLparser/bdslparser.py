#! python3

fileContents = []
noWhiteSpace = []
noCommentLines = []
noInlineComments = []
finishedLines = []

with open('./test_data/STM32F1_Med_density_LQFP48.bsd') as inputFile :
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
    if line[-1:] == ';' :
        tempLine = tempLine + line
        finishedLines.append(tempLine)
        tempLine = ''
    else :
        tempLine = tempLine + ' ' + line

for line in finishedLines :
    temp = line.split('&')
    temp = str.join(' ', temp)
    temp = temp.replace('\t', ' ')
    temp = temp.join(temp.split())
    temp = temp.strip()
    print(temp)
    #print(line)




