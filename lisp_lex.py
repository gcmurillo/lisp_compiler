import ply.lex as lex

# reserver words
reserved = {
	'SETQ': "setq",
	'DEFUN': "defun", 
	'QUOTE': "quote", 
	'SET': "set", 
	'T': "t", 
	'NIL': "nil", 
	'CAR': "car", 
	'CDR': "cdr", 
	'NTH': "nth", 
	'NTHCDR': "nthcdr", 
	'LAST': "last", 
	'LENGTH': "length", 
	'FIRST': "first", 
	'REST': "&rest",
	'OPTIONAL': "&optional", 
	'CONS': "const", 
	'APPEND': "append", 
	'INCR': "incr", 
	'DECR': "decr", 
	'PUSH': "push", 
	'NULL': "null", 
	'LAMBDA':"lambda",
	'DEFMACRO':"defmacro",
	'WRITE-LINE':"write-line",
	'TYPEP':"typep",
	'TYPE-OF':"type-of",
	'DEFVAR':"defvar",
	'WRITE':"write",
	'PROG':"prog",
	'DEFCONSTANT':"defconstant",
	'COND':"cond",
	'IF':"if",
	'WHEN':"when",
	'CASE':"case",
	'LOOP':"loop",
	'LOOP FOR':"loop for",
	'FROM':"from",
	'TO':"to",
	'DO':"do",
	'DOTIMES':"dotimes",

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