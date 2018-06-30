import ply.lex as lex

# reserver words
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
	'write-line':"WRITE-LINE",
	'typep':"TYPEP",
	'type-of':"TYPE-OF",
	'defvar':"DEFVAR",
	'write':"WRITE",
	'prog':"PROG",
	'defconstant': "DEFCONSTANT",
	'cond':"COND",
	'if': "IF",
	'when': "WHEN",
	'case':"CASE",
	'loop': "LOOP",
	'loop for':"LOOP FOR",
	'from': "FROM",
	'to': "TO",
	'do': "DO",
	'dotimes':"DOTIMES"
}

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
	'COMILLA_SIMPLE'
]

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'*'
t_DIVIDED = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_SYMBOLS = r'[a-z]\w*'
t_COMMENT = r';\s?\w[\w\s]*\n'
t_COMILLA_SIMPLE = r"\'"

def t_NUMBER(t):
	r'\d+'
	t.value = int(t.value)
	return t