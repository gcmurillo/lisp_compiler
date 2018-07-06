
import ply.yacc as yacc
from lisp_lex import tokens

""" Lambda Structure: 
    (lambda (arg-variables...)
       [documentation-string]
       [interactive-declaration]
       body-forms...)
"""


file = open('res', 'a')
file.close

def p_expresion_lambda(p):
    """expresion_lambda : LPAREN LAMBDA LPAREN arguments RPAREN TEXT body RPAREN 
    					| LPAREN LAMBDA LPAREN arguments RPAREN body RPAREN"""   
    print("Correct!")
    file = open('res', 'a')
    file.write("Correct!\n")
    file.close()

def p_body(p):
	""" body : expresion_list 
			 | expresion_list body 
             | factor"""

def p_expresion(p):
	""" expresion : LPAREN factor_list RPAREN 
                  | LPAREN operator factor_list  RPAREN
                  | LPAREN operator expresion_list RPAREN
                  | LPAREN FUNCTION factor_list RPAREN
                  | LPAREN FUNCTION expresion_list RPAREN
				  | LPAREN ifs RPAREN"""

def p_expresion_list(p):
    """ expresion_list : expresion
                       | expresion expresion_list 
                       | factor_list """

def p_ifs(p):
    """ ifs : IF booleans expresion expresion 
		    | IF expresion expresion expresion
		    | IF expresion expresion """

def p_arguments(p):
    """ arguments : symbol_list
                  | optional_list
                  | symbol_list optional_list
                  | rest_list 
                  | symbol_list rest_list 
                  | symbol_list optional_list rest_list """

def p_rest_list(p):
    # &rest option in argument list
    """ rest_list : REST symbol_list """

def p_optional_list(p):
    # &optional option in argument list
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
	             | EQUAL 
                 | GT
                 | LT
                 | GEQT 
                 | LEQT """

def p_booleans(p):
	""" booleans : T 
                 | NIL"""

def p_error(p):
    print("Syntax error!")
    print(p.value[0])
    file = open('res', 'a')
    file.write('Syntax error!\n')
    file.close()

parser = yacc.yacc()

'''
print("ENTER '(quit)' TO EXIT")
while True:
    try:
        s = input("lisp >>> ")
        if s == '(quit)':
            break
    except EOFError:
        break

    if not s: continue
    result = parser.parse(s)
'''

def validate(expr):
    return parser.parse(expr)

print("(lambda (x) (* x 5))")
validate("(lambda (x) (* x 5))") # correct

print("(lambda (x) (+ x 5 8 5))")
validate("(lambda (x) (+ x 5 8 5))") # correct

print("(lambda (x &optional y) (+ x y))")
validate("(lambda (x &optional y) (+ x y))") # correct

print("(lambda (x &optional y z) (/ x y z))")
validate("(lambda (x &optional y z) (/ x y z))") # correct

print("(lambda (x &optional y &optional z) (/ x y z))")
validate("(lambda (x &optional y &optional z) (/ x y z))") # incorrect

print("(lambda (x &optional y &rest z) (/ x y z))")
validate("(lambda (x &optional y &rest z) (/ x y z))") # correct

print("(lambda (x &optional y &rest z) (* (+ x 5) 5))")
validate("(lambda (x &optional y &rest z) (* (+ x 5) 5))") # correct

print("(lambda (x) (* (+ (+ x 5) 5) 5 6 6 5))") 
validate("(lambda (x) (* (+ (+ x 5) 5) 5 6 6 5))")  # correct

print("(lambda (x &rest y) (* (exp (+ x 5) 5)))") 
validate("(lambda (x &rest y) (* (exp (+ x 5) 5)))")  # correct

print("(lambda (&optional y) (if (y) (write y) (exp 2)))")
validate("(lambda (&optional y) (if (y) (write y) (exp 2)))") # correct