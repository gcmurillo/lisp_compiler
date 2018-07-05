
import ply.yacc as yacc
from lisp_lex import tokens

""" Lambda Structure: 
    (lambda (arg-variables...)
       [documentation-string]
       [interactive-declaration]
       body-forms...)
"""

def p_expresion_lambda(p):
    """expresion_lambda : LPAREN LAMBDA LPAREN arguments RPAREN TEXT body RPAREN 
    					| LPAREN LAMBDA LPAREN arguments RPAREN body RPAREN 
    					| LPAREN LAMBDA LPAREN RPAREN body RPAREN"""
    print("Correct!")

def p_body(p):
	""" body : expresion 
			 | expresion body """

def p_expresion(p):
	""" expresion : LPAREN expresion RPAREN 
				  | LPAREN operator factor_list RPAREN
				  | ifs """

def p_ifs(p):
	""" ifs : IF booleans expresion expresion 
		    | IF expresion expresion expresion
		    | IF expresion expresion """

def p_arguments(p):
    """ arguments : symbol_list
                  | arguments optional_list """

def p_optional_list(p):
    """ optional_list : OPTIONAL symbol_list """

def p_symbol_list(p):
    """ symbol_list : SYMBOL
                    | symbol_list SYMBOL """

def p_factor_list(p):
    """ factor_list : factor 
                    | factor_list factor"""

def p_factor(p):
    """ factor : SYMBOL 
               | NUMBER 
               | DECIMAL """

def p_operator(p):
	""" operator : PLUS 
                 | MINUS 
                 | TIMES
                 | DIVIDED 
	             | EQUAL"""

def p_booleans(p):
	""" booleans : T 
                 | NIL"""

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
