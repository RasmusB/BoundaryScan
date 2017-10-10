#! python3

import telnetlib

HOST = "localhost"
PORT = 4444

def scanChain(tn) :
    tn.write("scan_chain".encode('ascii') + b'\n')
    return tn.read_until(b'> ').decode('ascii')

with (telnetlib.Telnet(HOST, PORT)) as terminal:
    terminal.read_until(b"> ")
    print(scanChain(terminal))
