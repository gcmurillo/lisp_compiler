
import ply.yacc as yacc
from lisp_lex import tokens

""" Lambda Structure: 
    (lambda (arg-variables...)
       [documentation-string]
       [interactive-declaration]
       body-forms...)
"""

def p_expresion_lambda(p):
    """expresion : LPAREN LAMBDA LPAREN symbol_list RPAREN RPAREN """
    print("Correct!")

def p_expresion_plus(p):
    """expresion : LPAREN PLUS arguments RPAREN """
    print("correcto")


def p_arguments_multiple(p):
    """arguments : factor factor
                 | arguments factor"""

def p_symbol_list(p):
    """symbol_list : SYMBOL
                   | symbol_list SYMBOL"""

def p_factor(p):
    """factor : SYMBOL 
              | NUMBER 
              | DECIMAL """

def p_error(p):
    print("Syntax error!")


parser = yacc.yacc()
print("ENTER 'q' TO EXIT")
while True:
    try:
        s = input("lisp >>> ")
        if s == 'q':
            break
    except EOFError:
        break

    if not s: continue
    result = parser.parse(s)