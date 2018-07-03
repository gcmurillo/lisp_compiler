
import ply.yacc as yacc
from lisp_lex import tokens



def p_expresion_plus(p):
    """expresion : LPAREN PLUS factor factor RPAREN """
    p[0] = p[3] + p[4]


def p_factor(p):
    """factor : SYMBOL 
              | NUMBER 
              | DECIMAL """
    p[0] = p[1]


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
    print(result)