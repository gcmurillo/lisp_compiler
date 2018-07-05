import ply.lex as lex

# tokens
tokens = [
	'PLUS', # +
	'MINUS', # - 
	'TIMES', # *
	'DIVIDED', # /
	'LPAREN', # (
	'RPAREN', # )
	'SYMBOL', # variable names
	'COMMENT',  # ; cualquier cosa
	'NUMBER',
	'COMILLA_SIMPLE',
	'COMILLA_DOBLE',
	'TEXT',
	'DECIMAL',
	'EQUAL',
	'GT',
	'LT',
	'GEQT',
	'LEQT',
	'FUNCTION',
]

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDED = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_SYMBOL = r'[a-z]\w*'
t_COMMENT = r';\s*[\w][\w\s\:\.\_]*\n'
t_COMILLA_SIMPLE = r"\'"
t_COMILLA_DOBLE = r'\"'
t_TEXT = r"(\'[\w\s\.]*\'|\"[\w\s\.]*\")"
t_EQUAL = r'\='
t_GT = r'>'
t_LT = r'<'
t_GEQT = r'>='
t_LEQT = r'<=' 

reserved_words = {
	'&rest': "REST",
	'&optional': "OPTIONAL", 
	'if': "IF",
	'lambda':"LAMBDA",
	'cond':"COND",
	'when': "WHEN",
	'case':"CASE",
	'loop': "LOOP",
	'from': "FROM",
	'to': "TO",
	'do': "DO",
} 

constants = {
	'pi': 'PI',
	't': "T", 
	'nil': "NIL",
	'null': "NULL",
}

# reserved words
functions = {
	'setq': "SETQ",
	'defun': "DEFUN", 
	'quote': "QUOTE", 
	'write-line' : "WRITE_LINE",
	'set': "SET", 
	'car': "CAR",
	'exp': "EXP", 
	'cdr': "CDR", 
	'nth': "NTH", 
	'nthcdr': "NTHCDR", 
	'last': "LAST", 
	'length': "LENGTH", 
	'first': "FIRST", 
	'const': "CONST", 
	'append': "APPEND", 
	'incr': "INCR", 
	'decr': "DECR", 
	'push': "PUSH",
	'defmacro':"DEFMACRO",
	'typep':"TYPEP",
	'defvar':"DEFVAR",
	'write':"WRITE",
	'prog':"PROG",
	'defconstant': "DEFCONSTANT",
	'dotimes':"DOTIMES",
}

tokens = tokens + list(functions.values()) + list(reserved_words.values()) + list(constants.values())

def t_DECIMAL(t):
	r'\d+\.\d+'
	t.value = float(t.value)
	return t

def t_NUMBER(t):
	r'\d+'
	t.value = int(t.value)
	return t

def t_newline(t):
	r'\n+'
	t.lexer.lineno += len(t.value)

def t_ID(t):
	r'([a-z\-0-9]+|&optional|&rest)'
	if t.value in reserved_words:
    		t.type = reserved_words[t.value]
	elif t.value in constants:
    		t.type = 'NUMBER'
	elif t.value in functions:
    		t.type = 'FUNCTION'
	else:
    		t.type = 'SYMBOL'
	return t

t_ignore = ' \t'

def t_error(t):
	print("Incorrect character '%s'" % t.value[0])
	t.lexer.skip(1)

lexer = lex.lex()

'''
def test(code):
	lexer.input(code)
	while True:
		tok = lexer.token()
		if not tok:
			break
		print(tok)
'''
#test("((lambda (x) (* x x)) 1 2 3)")
#test("""(lambda (a b c) ; esto es un comentario
#		(+ a b c))""")

#test("(write-line 'hello')")

#test(""" ((lambda (n &optional n1) ; One required and one optional:
#                (if n1 (+ n n1) (1+ n))) ; 1 or 2 Arguments.
#              1 2) """)

#test("""(lambda (x)
#       "Return the hyperbolic cosine of X."
#       (* 0.5 (+ (exp x) (exp (- x)))))""")

#test("(lambda (x) (* pi 2))")