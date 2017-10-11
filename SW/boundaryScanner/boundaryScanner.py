#! python3

import telnetlib

HOST = "localhost"
PORT = 4444

class TapUnit :
    def __init__(self, num, name, enabled, IdCode, Expected, IrLen, IrCap, IrMask):
        self.no = num
        self.name = name
        if enabled == 'Y' :
            self.isEnabled = True
        else :
            self.isEnabled = False
        self.idCode = IdCode
        self.expected = Expected
        self.irLen = IrLen
        self.irCap = IrCap
        self.irMask = IrMask

def sendCommand(tn, command) :
    tn.write(command.encode('ascii') + b'\n')
    return tn.read_until(b'> ').decode('ascii')

def actOnResponse(response) :
    responseLines = response.splitlines()
    itemizedLines = []

    # Remove prompt and blank lines
    responseLines.remove('> ')
    while '' in responseLines :
        responseLines.remove('')

    # Remove excessive spaces
    for line in responseLines :
        itemizedLines.append( (' '.join(line.split())).split() )

    #print(itemizedLines)

    # Check what command was sent
    if itemizedLines[0][0] == 'scan_chain' :
        tapList = []
        # We sent a command to scan the entire chain and report
        # what TAPs were detected (if any).
        for items in itemizedLines[3:] :
            print(items)
            tapList.append(TapUnit(*items))
        print(tapList)


with (telnetlib.Telnet(HOST, PORT)) as terminal:
    terminal.read_until(b"> ")
    temp = sendCommand(terminal, "scan_chain")
    actOnResponse(temp)
