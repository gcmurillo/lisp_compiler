import ply.lex as lex

# tokens
tokens = [
	'PLUS', # +
	'MINUS', # - 
	'TIMES', # *
	'DIVIDED', # /
	'LPAREN', # (
	'RPAREN', # )
	'SYMBOLS', # variable names
	'COMMENT',  # ; cualquier cosa
	'NUMBER',
	'COMILLA_SIMPLE',
]

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDED = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_SYMBOLS = r'[a-z]\w*'
t_COMMENT = r';\s?\w[\w\s]*\n'
t_COMILLA_SIMPLE = r"\'"


# reserved words
reserved = {
	'setq': "SETQ",
	'defun': "DEFUN", 
	'quote': "QUOTE", 
	'set': "SET", 
	't': "T", 
	'nil': "NIL", 
	'car': "CAR", 
	'cdr': "CDR", 
	'nth': "NTH", 
	'nthcdr': "NTHCDR", 
	'last': "LAST", 
	'length': "LENGTH", 
	'first': "FIRST", 
	'&rest': "REST",
	'&optional': "OPTIONAL", 
	'const': "CONST", 
	'append': "APPEND", 
	'incr': "INCR", 
	'decr': "DECR", 
	'push': "PUSH", 
	'null': "NULL", 
	'lambda':"LAMBDA",
	'defmacro':"DEFMACRO",
	'typep':"TYPEP",
	'defvar':"DEFVAR",
	'write':"WRITE",
	'prog':"PROG",
	'defconstant': "DEFCONSTANT",
	'cond':"COND",
	'if': "IF",
	'when': "WHEN",
	'case':"CASE",
	'loop': "LOOP",
	'from': "FROM",
	'to': "TO",
	'do': "DO",
	'dotimes':"DOTIMES"
}

tokens = tokens + list(reserved.values())

def t_NUMBER(t):
	r'\d+'
	t.value = int(t.value)
	return t

def t_newline(t):
	r'\n+'
	t.lexer.lineno += len(t.value)

#TODO: validar variables con token SYMBOLS no ID
def t_ID(t):
	r'([a-z]+|&optional|&rest)'
	if t.value in reserved:
    		t.type = reserved[t.value]
	return t

t_ignore = ' '

def t_error(t):
	print("Incorrect character '%s'" % t.value[0])
	t.lexer.skip(1)

lexer = lex.lex()

code = "(lambda (x) (* x x)"

lexer.input(code)

while True:
	tok = lexer.token()
	if not tok:
		break
	print(tok)