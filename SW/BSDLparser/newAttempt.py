### Testing the default ANTLR VHDL parser

import sys
from antlr4 import *
from vhdlLexer import vhdlLexer
from vhdlParser import vhdlParser
from vhdlListener import vhdlListener


class vhdlPrintListener(vhdlListener):
    def enterPort(self, ctx):
        print("Port: %s" % ctx.ID())

def main(argv):
    input = FileStream(argv)
    lexer = vhdlLexer(input)
    stream = CommonTokenStream(lexer)
    parser = vhdlParser(stream)
    tree = parser.entity_declaration()
    pass # Debug breakpoint dummy instruction
    printer = vhdlPrintListener()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)
    pass # Debug breakpoint dummy instruction


if __name__ == '__main__':
    inputFile = './test_data/STM32F1_Med_density_LQFP48.bsd'
    if len(sys.argv) == 1:
        main(inputFile)
    else:
        main(sys.argv[1])
