from typing import Final
from types import MappingProxyType

KEYWORDS: frozenset = frozenset({
    'algoritmo', 'principal', 'variaveis',
    'constantes', 'registro', 'funcao',
    'retorno', 'vazio', 'se', 'senao',
    'enquanto', 'leia', 'escreva', 'inteiro',
    'real', 'booleano', 'char', 'cadeia',
    'verdadeiro', 'falso'
})

DELIMITERS: frozenset = frozenset({
    ',', '.', ';', '(', ')', '[', ']', '{', '}',
    '>', '>=', '<', '<=', '!=', '==', '=',
    '+', '-', '*', '/', '++', '--',
    '\n', ' ', '!', '&&', '||'
})

INVALID_TOKENS: frozenset = frozenset({
    '#', '$', '%', '\'', ':', '@',
    '\\', '^', '`', '_', '~', '?', 
})

TOKEN_MAL_FORMADO: Final = "TMF"
PALAVRA_RESERVADA: Final = "PRE"
INDENTIFICADOR: Final = "IDE"
NUMERO: Final = "NRO"
COMENTARIO: Final = "CoM"
CADEIA_DE_CARACTERES: Final = "CAC"
CADEIA_MAL_FORMADA: Final = "CMF"
OPERADOR_RELACIONAL: Final = "REL"
OPERADOR_LOGICO: Final = "LOG"
OPERADOR_ARITMETICO: Final = "ART"
DELIMITADOR: Final = "DEL"
COMENTARIO_MAL_FORMADO: Final = "CoMF"
NUMERO_MAL_FORMADO: Final = "NMF"
INDENTIFICADOR_MAL_FORMADO: Final = "IMF"
UNKNOWN_TOKEN: Final = "UNKNOWN"

__TOKENS: set[str] = {
    'TMF', 'PRE', 'IDE', 'NRO',
    'CoM', 'CAC', 'CMF', 'REL',
    'LOG', 'ART', 'DEL', 'CoMF',
    'NMF', 'IMF'
}

__TOKENS_DICT: dict[str, str] = {"t":'t'}

_SPECIAL_TYPES: dict[str, str] = {
    'NRO': 'NROpositivo',
    'IDE': 'IDE',
    'CAC': 'CAC',
    'CHAR': 'caractere' 
}

SPECIAL_TYPES: MappingProxyType = MappingProxyType(_SPECIAL_TYPES)

KEYS_SPECIAL_TYPES: tuple = (
    'NRO',
    'IDE',
    'CAC',
    'CHAR'
)

TO_IGNORE: tuple = (
    'funcao',
)

TOKENS: frozenset = frozenset(__TOKENS)

# VALID_SYMBOL: Final = lambda char: 126 <= ord(char) <= 32 and ord(char) != 34
# INVALID_SYMBOL: Final = True

# End Of Input Right Tokens
EOI_RIGHT_TOKENS: Final = '00 FINAL $\n'
EOI_RIGHT_TOKENS_NO_NEWLINE = '00 FINAL $'
SUCCESS_MESSAGE: Final = 'Sucesso!'

# TERMINALS: tuple = (
#     '(',
#     ')',
#     '$'
# )

# NON_TERMINALS: tuple = (
#     'S',
# )
_PARSER_ANALYSIS_TABLE:dict[tuple, list[str]] = {}
# _PARSER_ANALYSIS_TABLE['S', '('] = ['(', 'S', ')']
# _PARSER_ANALYSIS_TABLE['S', ')'] = ['None']
# _PARSER_ANALYSIS_TABLE['S', '$'] = ['None']

# TERMINALS = (
# 	'id',
# 	'+',
# 	'*',
# 	'(',
# 	')',
# 	'$'
# )

TERMINALS: tuple = (
    # ------ Palavras Reservadas ---------
    'algoritmo',
    'principal',
    'variaveis',
    'constantes',
    'registro',
    'funcao',
    'retorno',
    'vazio',
    'se',
    'senao',
    'enquanto',
    'leia',
    'escreva',
    'inteiro',
    'real',
    'booleano',
    'char',
    'cadeia',
    'verdadeiro',
    'falso',
    # -------- Operadores Aritmeticos--------------
    '+', '-', '*', '/', '++', '--',
    # -------  Operadores Relacionais--------------
    '!=', '==', '<', '<=', '>', '>=', '=',
    # -------  Operadores Logicos -----------------
    '!', '&&', '||',
    # -------  Delimitadores ----------------------
    ';', ',', '.', '(', ')', '[', ']', '{', '}',
    # -------  Numero -----------------------------
    'NROpositivo',
    # -------  Cadeia de caractere ---------------
    'CAC',
    #---------  Caractere -------------------------
    'caractere',
    #---------  Identificador ---------------------
    'IDE'
)

NON_TERMINALS = (
	'E',
	'E\'',
	'T',
	'T\'',
	'F'
)

# _PARSER_ANALYSIS_TABLE['E', 'id'] = ['T', 'E\'']
# _PARSER_ANALYSIS_TABLE['E', '(']  = ['T', 'E\'']
# _PARSER_ANALYSIS_TABLE['E\'', '+'] = ['+', 'T', 'E\'']
# _PARSER_ANALYSIS_TABLE['E\'', ')'] = ['None']
# _PARSER_ANALYSIS_TABLE['E\'', '$'] = ['None']
# _PARSER_ANALYSIS_TABLE['T', 'id'] = ['F', 'T\'']
# _PARSER_ANALYSIS_TABLE['T', '('] = ['F', 'T\'']
# _PARSER_ANALYSIS_TABLE['T\'', '+'] = ['None']
# _PARSER_ANALYSIS_TABLE['T\'', '*'] = [ '*', 'F', 'T\'']
# _PARSER_ANALYSIS_TABLE['T\'', ')'] = ['None']
# _PARSER_ANALYSIS_TABLE['T\'', '$'] = ['None']
# _PARSER_ANALYSIS_TABLE['F', 'id'] = [ 'id' ]
# _PARSER_ANALYSIS_TABLE['F', '('] = [ '(', 'E', ')' ]

_PARSER_ANALYSIS_TABLE['NRO', '-'] = [ '-', 'NROpositivo' ]
_PARSER_ANALYSIS_TABLE['NRO', 'NROpositivo'] = [ 'NROpositivo' ]
_PARSER_ANALYSIS_TABLE['IDEvetoroucompostoouchamada', 'IDE'] = [ 'IDE', 'vetoroucompostoouchamada' ]
_PARSER_ANALYSIS_TABLE['vetoroucompostoouchamada', '['] = [ '[', 'expressaonumerica', ']', 'vetoroucompostoouchamada' ]
_PARSER_ANALYSIS_TABLE['vetoroucompostoouchamada', '.'] = ['.', 'IDE', 'vetoroucompostoouchamada']
_PARSER_ANALYSIS_TABLE['vetoroucompostoouchamada', '('] = [ '(', 'listagemparametros', ')', 'vetoroucompostoouchamada' ]
_PARSER_ANALYSIS_TABLE['vetoroucompostoouchamada', '||'] = [ 'None' ]
_PARSER_ANALYSIS_TABLE['vetoroucompostoouchamada', '&&'] = [ 'None' ]
_PARSER_ANALYSIS_TABLE['vetoroucompostoouchamada', '=='] = [ 'None' ]
_PARSER_ANALYSIS_TABLE['vetoroucompostoouchamada', '!='] = [ 'None' ]
_PARSER_ANALYSIS_TABLE['vetoroucompostoouchamada', '>'] = [ 'None' ]
_PARSER_ANALYSIS_TABLE['vetoroucompostoouchamada', '<'] = [ 'None' ]
_PARSER_ANALYSIS_TABLE['vetoroucompostoouchamada', '>='] = [ 'None' ]
_PARSER_ANALYSIS_TABLE['vetoroucompostoouchamada', '<='] = [ 'None' ]
_PARSER_ANALYSIS_TABLE['vetoroucompostoouchamada', '+'] = [ 'None' ]
_PARSER_ANALYSIS_TABLE['vetoroucompostoouchamada', '-'] = [ 'None' ]
_PARSER_ANALYSIS_TABLE['vetoroucompostoouchamada', '*'] = [ 'None' ]
_PARSER_ANALYSIS_TABLE['vetoroucompostoouchamada', '/'] = [ 'None' ]
_PARSER_ANALYSIS_TABLE['vetoroucompostoouchamada', ','] = [ 'None' ]
_PARSER_ANALYSIS_TABLE['vetoroucompostoouchamada', ')'] = [ 'None' ]
_PARSER_ANALYSIS_TABLE['vetoroucompostoouchamada', ']'] = [ 'None' ]
_PARSER_ANALYSIS_TABLE['vetoroucompostoouchamada', ';'] = [ 'None' ]
_PARSER_ANALYSIS_TABLE['expressaobooleana', '!'] = [ 'expressaoAND', 'operacaoOR' ]
_PARSER_ANALYSIS_TABLE['expressaobooleana', 'verdadeiro'] = [ 'expressaoAND', 'operacaoOR' ]
_PARSER_ANALYSIS_TABLE['expressaobooleana', 'falso'] = [ 'expressaoAND', 'operacaoOR' ]
_PARSER_ANALYSIS_TABLE['expressaobooleana', 'IDE'] = [ 'expressaoAND', 'operacaoOR' ]
_PARSER_ANALYSIS_TABLE['expressaobooleana', '('] = [ 'expressaoAND', 'operacaoOR' ]
_PARSER_ANALYSIS_TABLE['operacaoOR', '||'] = [ '||', 'expressaobooleana' ]
_PARSER_ANALYSIS_TABLE['operacaoOR', ','] = [ 'None' ]
_PARSER_ANALYSIS_TABLE['operacaoOR', ';'] = [ 'None' ]
_PARSER_ANALYSIS_TABLE['operacaoOR', ')'] = [ 'None' ]
_PARSER_ANALYSIS_TABLE['expressaoAND', '!'] = [ 'expressaoNOT', 'operacaoAND' ]
_PARSER_ANALYSIS_TABLE['expressaoAND', 'verdadeiro'] = [ 'expressaoNOT', 'operacaoAND' ]
_PARSER_ANALYSIS_TABLE['expressaoAND', 'falso'] = [ 'expressaoNOT', 'operacaoAND' ]
_PARSER_ANALYSIS_TABLE['expressaoAND', 'IDE'] = [ 'expressaoNOT', 'operacaoAND' ]
_PARSER_ANALYSIS_TABLE['expressaoAND', '('] = [ 'expressaoNOT', 'operacaoAND' ]
_PARSER_ANALYSIS_TABLE['operacaoAND', '&&'] = [ '&&', 'expressaoAND' ]
_PARSER_ANALYSIS_TABLE['operacaoAND', '||'] = [ 'None' ]
_PARSER_ANALYSIS_TABLE['operacaoAND', ','] = [ 'None' ]
_PARSER_ANALYSIS_TABLE['operacaoAND', ';'] = [ 'None' ]
_PARSER_ANALYSIS_TABLE['operacaoAND', ')'] = [ 'None' ]
_PARSER_ANALYSIS_TABLE['expressaoNOT', '!'] = [ '!', 'parcelabooleana' ]
_PARSER_ANALYSIS_TABLE['expressaoNOT', 'verdadeiro'] = [ 'parcelabooleana' ]
_PARSER_ANALYSIS_TABLE['expressaoNOT', 'falso'] = [ 'parcelabooleana' ]
_PARSER_ANALYSIS_TABLE['expressaoNOT', 'IDE'] = [ 'parcelabooleana' ]
_PARSER_ANALYSIS_TABLE['expressaoNOT', '('] = [ 'parcelabooleana' ]
_PARSER_ANALYSIS_TABLE['parcelabooleana', 'verdadeiro'] = [ 'valorbooleano' ]
_PARSER_ANALYSIS_TABLE['parcelabooleana', 'falso'] = [ 'valorbooleano' ]
_PARSER_ANALYSIS_TABLE['parcelabooleana', 'IDE'] = [ 'valorbooleano' ]
_PARSER_ANALYSIS_TABLE['parcelabooleana', '('] = [ '(', 'valorbooleano', ')' ]
_PARSER_ANALYSIS_TABLE['valorbooleano', 'verdadeiro'] = [ 'verdadeiro' ]
_PARSER_ANALYSIS_TABLE['valorbooleano', 'falso'] = [ 'falso' ]
_PARSER_ANALYSIS_TABLE['valorbooleano', 'IDE'] = [ 'IDEvetoroucompostoouchamada' ]
_PARSER_ANALYSIS_TABLE['expressaonumerica', '('] = [ 'expressaoMD', 'operacaoAS' ]
_PARSER_ANALYSIS_TABLE['expressaonumerica', 'IDE'] = [ 'expressaoMD', 'operacaoAS' ]
_PARSER_ANALYSIS_TABLE['expressaonumerica', '-'] = [ 'expressaoMD', 'operacaoAS' ]
_PARSER_ANALYSIS_TABLE['expressaonumerica', 'NROpositivo'] = [ 'expressaoMD', 'operacaoAS' ]
_PARSER_ANALYSIS_TABLE['operacaoAS', '+'] = [ '+', 'expressaonumerica']
_PARSER_ANALYSIS_TABLE['operacaoAS', '-'] = ['-', 'expressaonumerica']
_PARSER_ANALYSIS_TABLE['operacaoAS', ','] = [ 'None' ]
_PARSER_ANALYSIS_TABLE['operacaoAS', ';'] = [ 'None' ]
_PARSER_ANALYSIS_TABLE['operacaoAS', ')'] = [ 'None' ]
_PARSER_ANALYSIS_TABLE['operacaoAS', ']'] = [ 'None' ]
_PARSER_ANALYSIS_TABLE['operacaoAS', '=='] = [ 'None' ]
_PARSER_ANALYSIS_TABLE['operacaoAS', '>'] = [ 'None' ]
_PARSER_ANALYSIS_TABLE['operacaoAS', '<'] = [ 'None' ]
_PARSER_ANALYSIS_TABLE['operacaoAS', '>='] = [ 'None' ]
_PARSER_ANALYSIS_TABLE['operacaoAS', '<='] = [ 'None' ]
_PARSER_ANALYSIS_TABLE['operacaoAS', '!='] = [ 'None' ]
_PARSER_ANALYSIS_TABLE['operacaoAS', '||'] = [ 'None' ]
_PARSER_ANALYSIS_TABLE['operacaoAS', '&&'] = [ 'None' ]
_PARSER_ANALYSIS_TABLE['expressaoMD', '('] = [ 'parcelanumerica', 'operacaoMD' ]
_PARSER_ANALYSIS_TABLE['expressaoMD', '-'] = [ 'parcelanumerica', 'operacaoMD' ]
_PARSER_ANALYSIS_TABLE['expressaoMD', 'NROpositivo'] = [ 'parcelanumerica', 'operacaoMD' ]
_PARSER_ANALYSIS_TABLE['expressaoMD', 'IDE'] = [ 'parcelanumerica', 'operacaoMD' ]
_PARSER_ANALYSIS_TABLE['operacaoMD', '*'] = [ '*', 'expressaoMD' ]
_PARSER_ANALYSIS_TABLE['operacaoMD', '/'] = [ '/', 'expressaoMD' ]
_PARSER_ANALYSIS_TABLE['operacaoMD', ','] = [ 'None' ]
_PARSER_ANALYSIS_TABLE['operacaoMD', ';'] = [ 'None' ]
_PARSER_ANALYSIS_TABLE['operacaoMD', ')'] = [ 'None' ]
_PARSER_ANALYSIS_TABLE['operacaoMD', ']'] = [ 'None' ]
_PARSER_ANALYSIS_TABLE['operacaoMD', '||'] = [ 'None' ]
_PARSER_ANALYSIS_TABLE['operacaoMD', '&&'] = [ 'None' ]
_PARSER_ANALYSIS_TABLE['operacaoMD', '=='] = [ 'None' ]
_PARSER_ANALYSIS_TABLE['operacaoMD', '!='] = [ 'None' ]
_PARSER_ANALYSIS_TABLE['operacaoMD', '>'] = [ 'None' ]
_PARSER_ANALYSIS_TABLE['operacaoMD', '<'] = [ 'None' ]
_PARSER_ANALYSIS_TABLE['operacaoMD', '>='] = [ 'None' ]
_PARSER_ANALYSIS_TABLE['operacaoMD', '<='] = [ 'None' ]
_PARSER_ANALYSIS_TABLE['operacaoMD', '+'] = [ 'None' ]
_PARSER_ANALYSIS_TABLE['operacaoMD', '-'] = [ 'None' ]
_PARSER_ANALYSIS_TABLE['parcelanumerica', '-'] = [ 'valornumerico' ]
_PARSER_ANALYSIS_TABLE['parcelanumerica', 'NROpositivo'] = [ 'valornumerico' ]
_PARSER_ANALYSIS_TABLE['parcelanumerica', 'IDE'] = [ 'valornumerico' ]
_PARSER_ANALYSIS_TABLE['parcelanumerica', '('] = [ '(', 'expressaonumerica', ')' ]
_PARSER_ANALYSIS_TABLE['valornumerico', '-'] = [ 'NRO' ]
_PARSER_ANALYSIS_TABLE['valornumerico', 'NROpositivo' ] = [ 'NRO' ]
_PARSER_ANALYSIS_TABLE['valornumerico', 'IDE' ] = [ 'IDEvetoroucompostoouchamada' ]
_PARSER_ANALYSIS_TABLE['declaracaobooleana', 'booleano'] = [ 'booleano', 'IDE', '=', 'expressaobooleana', 'listagemconstantebooleana', ';' ]
_PARSER_ANALYSIS_TABLE['listagemconstantebooleana', ','] = [ ',', 'IDE', '=', 'expressaobooleana', 'listagemconstantebooleana']
_PARSER_ANALYSIS_TABLE['listagemconstantebooleana', ';'] = [ 'None' ]
_PARSER_ANALYSIS_TABLE['declaracaonumerica', 'inteiro'] = [ 'inteiro', 'IDE', '=', 'expressaonumerica', 'listagemconstantenumerica', ';' ]
_PARSER_ANALYSIS_TABLE['declaracaonumerica', 'real'] = [ 'real', 'IDE', '=', 'expressaonumerica', 'listagemconstantenumerica', ';' ]
_PARSER_ANALYSIS_TABLE['listagemconstantenumerica', ','] = [',', 'IDE', '=', 'expressaonumerica', 'listagemconstantenumerica' ]
_PARSER_ANALYSIS_TABLE['listagemconstantenumerica', ';'] = [ 'None' ]
_PARSER_ANALYSIS_TABLE['declaracaodecadeia', 'cadeia'] = [ 'cadeia', 'IDE', '=', 'CACoucaractere', 'listagemconstantedecadeia', ';' ]
_PARSER_ANALYSIS_TABLE['CACoucaractere', 'CAC'] = [ 'CAC']
_PARSER_ANALYSIS_TABLE['CACoucaractere', 'caractere'] = [ 'caractere']
_PARSER_ANALYSIS_TABLE['listagemconstantedecadeia', ','] = [ ',', 'IDE', '=', 'CACoucaractere', 'listagemconstantedecadeia' ]
_PARSER_ANALYSIS_TABLE['listagemconstantedecadeia', ';'] = [ 'None' ]
_PARSER_ANALYSIS_TABLE['declaracaodecaractere', 'char'] = [ 'char', 'IDE', '=', 'caractere', 'listagemconstantedecaractere', ';' ]
_PARSER_ANALYSIS_TABLE['listagemconstantedecaractere', ','] = [ ',', 'IDE', '=', 'caractere', 'listagemconstantedecaractere' ]
_PARSER_ANALYSIS_TABLE['listagemconstantedecaractere', ';'] = [ 'None' ]
_PARSER_ANALYSIS_TABLE['declaracaodeconstante', 'booleano'] = ['declaracaobooleana' ]
_PARSER_ANALYSIS_TABLE['declaracaodeconstante', 'inteiro'] = ['declaracaonumerica' ]
_PARSER_ANALYSIS_TABLE['declaracaodeconstante', 'real'] = ['declaracaonumerica' ]
_PARSER_ANALYSIS_TABLE['declaracaodeconstante', 'cadeia'] = ['declaracaodecadeia' ]
_PARSER_ANALYSIS_TABLE['declaracaodeconstante', 'char'] = ['declaracaodecaractere' ]
_PARSER_ANALYSIS_TABLE['blocodeconstantes', 'constantes'] = [ 'constantes', '{', 'listagemblococonstantes', '}' ]
_PARSER_ANALYSIS_TABLE['listagemblococonstantes', 'booleano'] = [ 'declaracaodeconstante', 'listagemblococonstantes' ]
_PARSER_ANALYSIS_TABLE['listagemblococonstantes', 'inteiro'] = [ 'declaracaodeconstante', 'listagemblococonstantes' ]
_PARSER_ANALYSIS_TABLE['listagemblococonstantes', 'real'] = [ 'declaracaodeconstante', 'listagemblococonstantes' ]
_PARSER_ANALYSIS_TABLE['listagemblococonstantes', 'cadeia'] = [ 'declaracaodeconstante', 'listagemblococonstantes' ]
_PARSER_ANALYSIS_TABLE['listagemblococonstantes', 'char'] = [ 'declaracaodeconstante', 'listagemblococonstantes' ]
_PARSER_ANALYSIS_TABLE['listagemblococonstantes', '}'] = ['None']
_PARSER_ANALYSIS_TABLE['declaracaodevariavel', 'IDE'] = [ 'IDE', 'IDEvetor', 'listagemdeidentificador', ';' ]
_PARSER_ANALYSIS_TABLE['declaracaodevariavel', 'inteiro'] = [ 'inteiro', 'IDEvetor', 'listagemdeidentificador', ';' ]
_PARSER_ANALYSIS_TABLE['declaracaodevariavel', 'real'] = [ 'real', 'IDEvetor', 'listagemdeidentificador', ';' ]
_PARSER_ANALYSIS_TABLE['declaracaodevariavel', 'char'] = [ 'char', 'IDEvetor', 'listagemdeidentificador', ';' ]
_PARSER_ANALYSIS_TABLE['declaracaodevariavel', 'cadeia'] = [ 'cadeia', 'IDEvetor', 'listagemdeidentificador', ';' ]
_PARSER_ANALYSIS_TABLE['declaracaodevariavel', 'booleano'] = [ 'booleano', 'IDEvetor', 'listagemdeidentificador', ';' ]
_PARSER_ANALYSIS_TABLE['IDEvetor', 'IDE'] = [ 'IDE', 'vetor' ]
_PARSER_ANALYSIS_TABLE['vetor', '['] = ['[', 'expressaonumerica',']', 'vetor' ]
_PARSER_ANALYSIS_TABLE['vetor', ',' ] = [ 'None' ]
_PARSER_ANALYSIS_TABLE['vetor', ';' ] = [ 'None' ]
_PARSER_ANALYSIS_TABLE['vetor', ')' ] = [ 'None' ]
_PARSER_ANALYSIS_TABLE['listagemdeidentificador', ','] = [ ',', 'IDEvetor', 'listagemdeidentificador' ]
_PARSER_ANALYSIS_TABLE['listagemdeidentificador', 'IDE'] = [ 'None' ]
_PARSER_ANALYSIS_TABLE['listagemdeidentificador', 'booleano'] = [ 'None' ]
_PARSER_ANALYSIS_TABLE['listagemdeidentificador', 'inteiro'] = [ 'None' ]
_PARSER_ANALYSIS_TABLE['listagemdeidentificador', 'real'] = [ 'None' ]
_PARSER_ANALYSIS_TABLE['listagemdeidentificador', 'cadeia'] = [ 'None' ]
_PARSER_ANALYSIS_TABLE['listagemdeidentificador', 'char'] = [ 'None' ]
_PARSER_ANALYSIS_TABLE['listagemdeidentificador', '}'] = [ 'None' ]
_PARSER_ANALYSIS_TABLE['listagemdeidentificador', ';'] = [ 'None' ]
_PARSER_ANALYSIS_TABLE['blocodevariaveis', 'variaveis'] = [ 'variaveis', '{', 'listagemblocovariaveis', '}' ]
_PARSER_ANALYSIS_TABLE['listagemblocovariaveis', 'IDE'] = [ 'declaracaodevariavel', 'listagemblocovariaveis' ]
_PARSER_ANALYSIS_TABLE['listagemblocovariaveis', 'booleano'] = [ 'declaracaodevariavel', 'listagemblocovariaveis' ]
_PARSER_ANALYSIS_TABLE['listagemblocovariaveis', 'inteiro'] = [ 'declaracaodevariavel', 'listagemblocovariaveis' ]
_PARSER_ANALYSIS_TABLE['listagemblocovariaveis', 'real'] = [ 'declaracaodevariavel', 'listagemblocovariaveis' ]
_PARSER_ANALYSIS_TABLE['listagemblocovariaveis', 'cadeia'] = [ 'declaracaodevariavel', 'listagemblocovariaveis' ]
_PARSER_ANALYSIS_TABLE['listagemblocovariaveis', 'char'] = [ 'declaracaodevariavel', 'listagemblocovariaveis' ]
_PARSER_ANALYSIS_TABLE['listagemblocovariaveis', '}'] = ['None']
_PARSER_ANALYSIS_TABLE['blocoderegistro', 'registro'] = [ 'registro', 'IDE', '{', 'listagemblocovariaveis', '}' ]
_PARSER_ANALYSIS_TABLE['reatribuicao', 'IDE'] = [ 'IDE', 'reatribuicaosimplesouvetoroucomposto', ';' ]
_PARSER_ANALYSIS_TABLE['reatribuicaosimplesouvetoroucomposto', '['] = [ '[', 'expressaonumerica', ']', 'reatribuicaosimplesouvetoroucomposto' ]
_PARSER_ANALYSIS_TABLE['reatribuicaosimplesouvetoroucomposto', '.'] = [ '.', 'IDE', 'reatribuicaosimplesouvetoroucomposto' ]
_PARSER_ANALYSIS_TABLE['reatribuicaosimplesouvetoroucomposto', '='] = [ '=', 'expressaogeral' ]
_PARSER_ANALYSIS_TABLE['listagemparametros', '!'] = [ 'expressaogeral', 'maisparametros' ]
_PARSER_ANALYSIS_TABLE['listagemparametros', 'IDE'] = [ 'expressaogeral', 'maisparametros' ]
_PARSER_ANALYSIS_TABLE['listagemparametros', 'verdadeiro'] = [ 'expressaogeral', 'maisparametros' ]
_PARSER_ANALYSIS_TABLE['listagemparametros', 'falso'] = [ 'expressaogeral', 'maisparametros' ]
_PARSER_ANALYSIS_TABLE['listagemparametros', '-'] = [ 'expressaogeral', 'maisparametros' ]
_PARSER_ANALYSIS_TABLE['listagemparametros', 'NROpositivo'] = [ 'expressaogeral', 'maisparametros' ]
_PARSER_ANALYSIS_TABLE['listagemparametros', 'CAC'] = [ 'expressaogeral', 'maisparametros' ]
_PARSER_ANALYSIS_TABLE['listagemparametros', 'caractere'] = [ 'expressaogeral', 'maisparametros' ]
_PARSER_ANALYSIS_TABLE['listagemparametros', '('] = [ 'expressaogeral', 'maisparametros' ]
_PARSER_ANALYSIS_TABLE['listagemparametros', ')'] = [ 'None' ]
_PARSER_ANALYSIS_TABLE['maisparametros', ','] = [ ',', 'expressaogeral', 'maisparametros' ]
_PARSER_ANALYSIS_TABLE['maisparametros', ')'] = [ 'None' ]
_PARSER_ANALYSIS_TABLE['retornov', 'retorno'] = [ 'retorno', 'valorretorno', ';' ]
_PARSER_ANALYSIS_TABLE['valorretorno', '!'] = [ 'expressaogeral' ]
_PARSER_ANALYSIS_TABLE['valorretorno', 'IDE'] = [ 'expressaogeral' ]
_PARSER_ANALYSIS_TABLE['valorretorno', 'verdadeiro'] = [ 'expressaogeral' ]
_PARSER_ANALYSIS_TABLE['valorretorno', 'falso'] = [ 'expressaogeral' ]
_PARSER_ANALYSIS_TABLE['valorretorno', '-'] = [ 'expressaogeral' ]
_PARSER_ANALYSIS_TABLE['valorretorno', 'NROpositivo'] = [ 'expressaogeral' ]
_PARSER_ANALYSIS_TABLE['valorretorno', 'CAC'] = [ 'expressaogeral' ]
_PARSER_ANALYSIS_TABLE['valorretorno', 'caractere'] = [ 'expressaogeral' ]
_PARSER_ANALYSIS_TABLE['valorretorno', '('] = [ 'expressaogeral' ]
_PARSER_ANALYSIS_TABLE['valorretorno', ';'] = [ 'None' ]
_PARSER_ANALYSIS_TABLE['escrevav', 'escreva'] = [ 'escreva', '(', 'listagemparametros', ')', ';' ]
_PARSER_ANALYSIS_TABLE['leiav', 'leia'] = [ 'leia', '(', 'listagemleia', ')', ';' ]
_PARSER_ANALYSIS_TABLE['listagemleia', 'IDE'] = [ 'IDEvetoroucompostoouchamada', 'maisparametrosleia' ]
_PARSER_ANALYSIS_TABLE['maisparametrosleia', ','] = [ ',', 'IDEvetoroucompostoouchamada', 'maisparametrosleia' ]
_PARSER_ANALYSIS_TABLE['maisparametrosleia', ')'] = ['None']
_PARSER_ANALYSIS_TABLE['algoritmov', 'algoritmo'] = ['algoritmo', '{', 'corpo', '}']
_PARSER_ANALYSIS_TABLE['corpo', 'constantes'] = [ 'blocodeconstantes', 'corpovariaveis' ]
_PARSER_ANALYSIS_TABLE['corpo', 'variaveis'] = [ 'corpovariaveis' ]
_PARSER_ANALYSIS_TABLE['corpo', 'registro'] = [ 'corpovariaveis' ]
_PARSER_ANALYSIS_TABLE['corpo', 'booleano'] = [ 'corpovariaveis' ]
_PARSER_ANALYSIS_TABLE['corpo', 'inteiro'] = [ 'corpovariaveis' ]
_PARSER_ANALYSIS_TABLE['corpo', 'real'] = [ 'corpovariaveis' ]
_PARSER_ANALYSIS_TABLE['corpo', 'char'] = [ 'corpovariaveis' ]
_PARSER_ANALYSIS_TABLE['corpo', 'cadeia'] = [ 'corpovariaveis' ]
_PARSER_ANALYSIS_TABLE['corpo', 'IDE'] = [ 'corpovariaveis' ]
_PARSER_ANALYSIS_TABLE['corpo', 'vazio'] = [ 'corpovariaveis' ]
_PARSER_ANALYSIS_TABLE['corpo', '}'] = [ 'None' ]
_PARSER_ANALYSIS_TABLE['corpovariaveis', 'variaveis'] = [ 'blocodevariaveis', 'corpocomposto' ]
_PARSER_ANALYSIS_TABLE['corpovariaveis', 'registro'] = [ 'corpocomposto' ]
_PARSER_ANALYSIS_TABLE['corpovariaveis', 'booleano'] = [ 'corpocomposto' ]
_PARSER_ANALYSIS_TABLE['corpovariaveis', 'inteiro'] = [ 'corpocomposto' ]
_PARSER_ANALYSIS_TABLE['corpovariaveis', 'real'] = [ 'corpocomposto' ]
_PARSER_ANALYSIS_TABLE['corpovariaveis', 'char'] = [ 'corpocomposto' ]
_PARSER_ANALYSIS_TABLE['corpovariaveis', 'cadeia'] = [ 'corpocomposto' ]
_PARSER_ANALYSIS_TABLE['corpovariaveis', 'IDE'] = [ 'corpocomposto' ]
_PARSER_ANALYSIS_TABLE['corpovariaveis', 'vazio'] = [ 'corpocomposto' ]
_PARSER_ANALYSIS_TABLE['corpovariaveis', '}'] = ['None']
_PARSER_ANALYSIS_TABLE['corpocomposto', 'registro'] = [ 'listagemderegistro', 'listagemdefuncoes' ]
_PARSER_ANALYSIS_TABLE['corpocomposto', 'booleano'] = [ 'listagemderegistro', 'listagemdefuncoes' ]
_PARSER_ANALYSIS_TABLE['corpocomposto', 'inteiro'] = [ 'listagemderegistro', 'listagemdefuncoes' ]
_PARSER_ANALYSIS_TABLE['corpocomposto', 'real'] = [ 'listagemderegistro', 'listagemdefuncoes' ]
_PARSER_ANALYSIS_TABLE['corpocomposto', 'char'] = [ 'listagemderegistro', 'listagemdefuncoes' ]
_PARSER_ANALYSIS_TABLE['corpocomposto', 'cadeia'] = [ 'listagemderegistro', 'listagemdefuncoes' ]
_PARSER_ANALYSIS_TABLE['corpocomposto', 'IDE'] = [ 'listagemderegistro', 'listagemdefuncoes' ]
_PARSER_ANALYSIS_TABLE['corpocomposto', 'vazio'] = [ 'listagemderegistro', 'listagemdefuncoes' ]
_PARSER_ANALYSIS_TABLE['corpocomposto', '}'] = ['None']
_PARSER_ANALYSIS_TABLE['listagemderegistro', 'registro'] = [ 'blocoderegistro', 'listagemderegistro' ]
_PARSER_ANALYSIS_TABLE['listagemderegistro', 'booleano'] = [ 'None' ]
_PARSER_ANALYSIS_TABLE['listagemderegistro', 'inteiro'] = [ 'None' ]
_PARSER_ANALYSIS_TABLE['listagemderegistro', 'real'] = [ 'None' ]
_PARSER_ANALYSIS_TABLE['listagemderegistro', 'char'] = [ 'None' ]
_PARSER_ANALYSIS_TABLE['listagemderegistro', 'cadeia'] = [ 'None' ]
_PARSER_ANALYSIS_TABLE['listagemderegistro', 'IDE'] = [ 'None' ]
_PARSER_ANALYSIS_TABLE['listagemderegistro', 'vazio'] = [ 'None' ]
_PARSER_ANALYSIS_TABLE['listagemdefuncoes', 'booleano'] = [ 'tiposretorno', 'funcaoouprincipal' ]
_PARSER_ANALYSIS_TABLE['listagemdefuncoes', 'inteiro'] = [ 'tiposretorno', 'funcaoouprincipal' ]
_PARSER_ANALYSIS_TABLE['listagemdefuncoes', 'real'] = [ 'tiposretorno', 'funcaoouprincipal' ]
_PARSER_ANALYSIS_TABLE['listagemdefuncoes', 'char'] = [ 'tiposretorno', 'funcaoouprincipal' ]
_PARSER_ANALYSIS_TABLE['listagemdefuncoes', 'IDE'] = [ 'tiposretorno', 'funcaoouprincipal' ]
_PARSER_ANALYSIS_TABLE['listagemdefuncoes', 'cadeia'] = [ 'tiposretorno', 'funcaoouprincipal' ]
_PARSER_ANALYSIS_TABLE['listagemdefuncoes', 'vazio'] = [ 'tiposretorno', 'funcaoouprincipal' ]
_PARSER_ANALYSIS_TABLE['funcaoouprincipal', 'IDE'] = [ 'funcaoordinaria', 'listagemdefuncoes' ]
_PARSER_ANALYSIS_TABLE['funcaoouprincipal', 'principal'] = [ 'funcaoprincipal' ]
_PARSER_ANALYSIS_TABLE['escopo', 'constantes'] = [ 'blocodeconstantes', 'escopovariaveis' ]
_PARSER_ANALYSIS_TABLE['escopo', 'variaveis'] = [ 'escopovariaveis' ]
_PARSER_ANALYSIS_TABLE['escopo', 'se'] = [ 'escopovariaveis' ]
_PARSER_ANALYSIS_TABLE['escopo', 'enquanto'] = [ 'escopovariaveis' ]
_PARSER_ANALYSIS_TABLE['escopo', 'leia'] = [ 'escopovariaveis' ]
_PARSER_ANALYSIS_TABLE['escopo', 'escreva'] = [ 'escopovariaveis' ]
_PARSER_ANALYSIS_TABLE['escopo', 'retorno'] = [ 'escopovariaveis' ]
_PARSER_ANALYSIS_TABLE['escopo', 'IDE'] = [ 'escopovariaveis' ]
_PARSER_ANALYSIS_TABLE['escopo', '}'] = [ 'None' ]
_PARSER_ANALYSIS_TABLE['escopovariaveis', 'variaveis'] = [ 'blocodevariaveis', 'bloco', 'retornov' ]
_PARSER_ANALYSIS_TABLE['escopovariaveis', 'se'] = [ 'bloco', 'retornov' ]
_PARSER_ANALYSIS_TABLE['escopovariaveis', 'enquanto'] = [ 'bloco', 'retornov' ]
_PARSER_ANALYSIS_TABLE['escopovariaveis', 'leia'] = [ 'bloco', 'retornov' ]
_PARSER_ANALYSIS_TABLE['escopovariaveis', 'escreva'] = [ 'bloco', 'retornov' ]
_PARSER_ANALYSIS_TABLE['escopovariaveis', 'IDE'] = [ 'bloco', 'retornov' ]
_PARSER_ANALYSIS_TABLE['escopovariaveis', 'retorno'] = [ 'bloco', 'retornov' ]
_PARSER_ANALYSIS_TABLE['escopovariaveis', '}'] = [ 'None' ]
_PARSER_ANALYSIS_TABLE['bloco', 'se'] = [ 'sev', 'bloco' ]
_PARSER_ANALYSIS_TABLE['bloco', 'enquanto'] = [ 'enquantov', 'bloco' ]
_PARSER_ANALYSIS_TABLE['bloco', 'leia'] = [ 'leiav', 'bloco' ]
_PARSER_ANALYSIS_TABLE['bloco', 'escreva'] = [ 'escrevav', 'bloco' ]
_PARSER_ANALYSIS_TABLE['bloco', 'IDE'] = [ 'reatribuicao', 'bloco' ]
_PARSER_ANALYSIS_TABLE['bloco', '}'] = [ 'None' ]
_PARSER_ANALYSIS_TABLE['bloco', 'retorno'] = [ 'None' ]
_PARSER_ANALYSIS_TABLE['sev', 'se'] = [ 'se', '(', 'expressaogeral', ')', '{', 'bloco', '}', 'senaov' ]
_PARSER_ANALYSIS_TABLE['senaov', 'senao'] = [ 'senao', '{', 'bloco', '}' ]
_PARSER_ANALYSIS_TABLE['senaov', 'se'] = [ 'None' ]
_PARSER_ANALYSIS_TABLE['senaov', 'enquanto'] = [ 'None' ]
_PARSER_ANALYSIS_TABLE['senaov', 'leia'] = [ 'None' ]
_PARSER_ANALYSIS_TABLE['senaov', 'escreva'] = [ 'None' ]
_PARSER_ANALYSIS_TABLE['senaov', 'IDE'] = [ 'None' ]
_PARSER_ANALYSIS_TABLE['senaov', '}'] = [ 'None' ]
_PARSER_ANALYSIS_TABLE['senaov', 'retorno'] = [ 'None' ]
_PARSER_ANALYSIS_TABLE['enquantov', 'enquanto'] = [ 'enquanto', '(', 'expressaogeral', ')', '{', 'bloco', '}' ]
_PARSER_ANALYSIS_TABLE['funcaoordinaria', 'IDE'] = [ 'IDE', '(', 'listagemdeclaracaoparametros', ')', '{', 'escopo', '}' ]
_PARSER_ANALYSIS_TABLE['funcaoprincipal', 'principal'] = ['principal', '(', 'listagemdeclaracaoparametros', ')', '{', 'escopo', '}' ]
_PARSER_ANALYSIS_TABLE['listagemdeclaracaoparametros', 'booleano'] = [ 'tipos', 'IDEvetor', 'maisdeclaracaoparametros' ]
_PARSER_ANALYSIS_TABLE['listagemdeclaracaoparametros', 'inteiro'] = [ 'tipos', 'IDEvetor', 'maisdeclaracaoparametros' ]
_PARSER_ANALYSIS_TABLE['listagemdeclaracaoparametros', 'real'] = [ 'tipos', 'IDEvetor', 'maisdeclaracaoparametros' ]
_PARSER_ANALYSIS_TABLE['listagemdeclaracaoparametros', 'char'] = [ 'tipos', 'IDEvetor', 'maisdeclaracaoparametros' ]
_PARSER_ANALYSIS_TABLE['listagemdeclaracaoparametros', 'cadeia'] = [ 'tipos', 'IDEvetor', 'maisdeclaracaoparametros' ]
_PARSER_ANALYSIS_TABLE['listagemdeclaracaoparametros', 'IDE'] = [ 'tipos', 'IDEvetor', 'maisdeclaracaoparametros' ]
_PARSER_ANALYSIS_TABLE['maisdeclaracaoparametros', ','] = [ ',', 'tipos', 'IDEvetor', 'maisdeclaracaoparametros'  ]
_PARSER_ANALYSIS_TABLE['maisdeclaracaoparametros', ')'] = [ 'None' ]
_PARSER_ANALYSIS_TABLE['listagemdeclaracaoparametros', ')'] = [ 'None' ]
_PARSER_ANALYSIS_TABLE['tipos', 'booleano'] = ['booleano']
_PARSER_ANALYSIS_TABLE['tipos', 'inteiro'] = ['inteiro']
_PARSER_ANALYSIS_TABLE['tipos', 'real'] = ['real']
_PARSER_ANALYSIS_TABLE['tipos', 'char'] = ['char']
_PARSER_ANALYSIS_TABLE['tipos', 'cadeia'] = ['cadeia']
_PARSER_ANALYSIS_TABLE['tipos', 'IDE'] = ['IDE']
_PARSER_ANALYSIS_TABLE['tiposretorno', 'booleano'] = ['booleano']
_PARSER_ANALYSIS_TABLE['tiposretorno', 'inteiro'] = ['inteiro']
_PARSER_ANALYSIS_TABLE['tiposretorno', 'real'] = ['real']
_PARSER_ANALYSIS_TABLE['tiposretorno', 'char'] = ['char']
_PARSER_ANALYSIS_TABLE['tiposretorno', 'cadeia'] = ['cadeia']
_PARSER_ANALYSIS_TABLE['tiposretorno', 'IDE'] = ['IDE']
_PARSER_ANALYSIS_TABLE['tiposretorno', 'vazio'] = [ 'vazio' ]
_PARSER_ANALYSIS_TABLE['expressaogeral', '!'] = [ 'expressaoANDgeral', 'operacaoORgeral' ]
_PARSER_ANALYSIS_TABLE['expressaogeral', 'IDE'] = [ 'expressaoANDgeral', 'operacaoORgeral' ]
_PARSER_ANALYSIS_TABLE['expressaogeral', 'verdadeiro'] = [ 'expressaoANDgeral', 'operacaoORgeral' ]
_PARSER_ANALYSIS_TABLE['expressaogeral', 'falso'] = [ 'expressaoANDgeral', 'operacaoORgeral' ]
_PARSER_ANALYSIS_TABLE['expressaogeral', '-'] = [ 'expressaoANDgeral', 'operacaoORgeral' ]
_PARSER_ANALYSIS_TABLE['expressaogeral', 'NROpositivo'] = [ 'expressaoANDgeral', 'operacaoORgeral' ]
_PARSER_ANALYSIS_TABLE['expressaogeral', 'CAC'] = [ 'expressaoANDgeral', 'operacaoORgeral' ]
_PARSER_ANALYSIS_TABLE['expressaogeral', 'caractere'] = [ 'expressaoANDgeral', 'operacaoORgeral' ]
_PARSER_ANALYSIS_TABLE['expressaogeral', '('] = [ 'expressaoANDgeral', 'operacaoORgeral' ]
_PARSER_ANALYSIS_TABLE['operacaoORgeral', '||'] = [ '||', 'expressaogeral' ]
_PARSER_ANALYSIS_TABLE['operacaoORgeral', ';'] = [ 'None' ]
_PARSER_ANALYSIS_TABLE['operacaoORgeral', ','] = [ 'None' ]
_PARSER_ANALYSIS_TABLE['operacaoORgeral', ')'] = [ 'None' ]
_PARSER_ANALYSIS_TABLE['expressaoANDgeral', '!'] = [ 'expressaoRELgeral', 'operacaoANDgeral' ]
_PARSER_ANALYSIS_TABLE['expressaoANDgeral', 'IDE'] = [ 'expressaoRELgeral', 'operacaoANDgeral' ]
_PARSER_ANALYSIS_TABLE['expressaoANDgeral', 'verdadeiro'] = [ 'expressaoRELgeral', 'operacaoANDgeral' ]
_PARSER_ANALYSIS_TABLE['expressaoANDgeral', 'falso'] = [ 'expressaoRELgeral', 'operacaoANDgeral' ]
_PARSER_ANALYSIS_TABLE['expressaoANDgeral', '-'] = [ 'expressaoRELgeral', 'operacaoANDgeral' ]
_PARSER_ANALYSIS_TABLE['expressaoANDgeral', 'NROpositivo'] = [ 'expressaoRELgeral', 'operacaoANDgeral' ]
_PARSER_ANALYSIS_TABLE['expressaoANDgeral', 'CAC'] = [ 'expressaoRELgeral', 'operacaoANDgeral' ]
_PARSER_ANALYSIS_TABLE['expressaoANDgeral', 'caractere'] = [ 'expressaoRELgeral', 'operacaoANDgeral' ]
_PARSER_ANALYSIS_TABLE['expressaoANDgeral', '('] = [ 'expressaoRELgeral', 'operacaoANDgeral' ]
_PARSER_ANALYSIS_TABLE['operacaoANDgeral', '&&'] = [ '&&', 'expressaoANDgeral' ]
_PARSER_ANALYSIS_TABLE['operacaoANDgeral', '||'] = [ 'None' ]
_PARSER_ANALYSIS_TABLE['operacaoANDgeral', ','] = [ 'None' ]
_PARSER_ANALYSIS_TABLE['operacaoANDgeral', ';'] = [ 'None' ]
_PARSER_ANALYSIS_TABLE['operacaoANDgeral', ')'] = [ 'None' ]
_PARSER_ANALYSIS_TABLE['expressaoRELgeral', '!'] = [ 'expressaoNOTgeral', 'operacaoRELgeral' ]
_PARSER_ANALYSIS_TABLE['expressaoRELgeral', 'verdadeiro'] = [ 'expressaoNOTgeral', 'operacaoRELgeral' ]
_PARSER_ANALYSIS_TABLE['expressaoRELgeral', 'falso'] = [ 'expressaoNOTgeral', 'operacaoRELgeral' ]
_PARSER_ANALYSIS_TABLE['expressaoRELgeral', 'IDE'] = [ 'expressaoNOTgeral', 'operacaoRELgeral' ]
_PARSER_ANALYSIS_TABLE['expressaoRELgeral', '-'] = [ 'expressaoNOTgeral', 'operacaoRELgeral' ]
_PARSER_ANALYSIS_TABLE['expressaoRELgeral', 'NROpositivo'] = [ 'expressaoNOTgeral', 'operacaoRELgeral' ]
_PARSER_ANALYSIS_TABLE['expressaoRELgeral', 'CAC'] = [ 'expressaoNOTgeral', 'operacaoRELgeral' ]
_PARSER_ANALYSIS_TABLE['expressaoRELgeral', 'caractere'] = [ 'expressaoNOTgeral', 'operacaoRELgeral' ]
_PARSER_ANALYSIS_TABLE['expressaoRELgeral', '('] = [ 'expressaoNOTgeral', 'operacaoRELgeral' ]
_PARSER_ANALYSIS_TABLE['operacaoRELgeral', '=='] = [ '==', 'expressaoNOTgeral' ]
_PARSER_ANALYSIS_TABLE['operacaoRELgeral', '!='] = [ '!=', 'expressaoNOTgeral' ]
_PARSER_ANALYSIS_TABLE['operacaoRELgeral', '>'] = [ '>', 'expressaoNOTgeral' ]
_PARSER_ANALYSIS_TABLE['operacaoRELgeral', '<'] = [ '<', 'expressaoNOTgeral' ]
_PARSER_ANALYSIS_TABLE['operacaoRELgeral', '>='] = [ '>=', 'expressaoNOTgeral' ]
_PARSER_ANALYSIS_TABLE['operacaoRELgeral', '<='] = [ '<=', 'expressaoNOTgeral' ]
_PARSER_ANALYSIS_TABLE['operacaoRELgeral', '&&'] = ['None' ]
_PARSER_ANALYSIS_TABLE['operacaoRELgeral', '||'] = ['None' ]
_PARSER_ANALYSIS_TABLE['operacaoRELgeral', ','] = ['None' ]
_PARSER_ANALYSIS_TABLE['operacaoRELgeral', ';'] = ['None' ]
_PARSER_ANALYSIS_TABLE['operacaoRELgeral', ')'] = ['None' ]
_PARSER_ANALYSIS_TABLE['expressaoNOTgeral', '!'] = [ '!', 'parcelabooleana' ]
_PARSER_ANALYSIS_TABLE['expressaoNOTgeral', 'IDE'] = [ 'expressaoASgeral' ]
_PARSER_ANALYSIS_TABLE['expressaoNOTgeral', 'verdadeiro'] = [ 'expressaoASgeral' ]
_PARSER_ANALYSIS_TABLE['expressaoNOTgeral', 'falso'] = [ 'expressaoASgeral' ]
_PARSER_ANALYSIS_TABLE['expressaoNOTgeral', '-'] = [ 'expressaoASgeral' ]
_PARSER_ANALYSIS_TABLE['expressaoNOTgeral', 'NROpositivo'] = [ 'expressaoASgeral' ]
_PARSER_ANALYSIS_TABLE['expressaoNOTgeral', 'CAC'] = [ 'expressaoASgeral' ]
_PARSER_ANALYSIS_TABLE['expressaoNOTgeral', 'caractere'] = [ 'expressaoASgeral' ]
_PARSER_ANALYSIS_TABLE['expressaoNOTgeral', '('] = [ 'expressaoASgeral' ]
_PARSER_ANALYSIS_TABLE['expressaoASgeral', 'IDE'] = [ 'expressaoMDgeral', 'operacaoASgeral' ]
_PARSER_ANALYSIS_TABLE['expressaoASgeral', 'verdadeiro'] = [ 'expressaoMDgeral', 'operacaoASgeral' ]
_PARSER_ANALYSIS_TABLE['expressaoASgeral', 'falso'] = [ 'expressaoMDgeral', 'operacaoASgeral' ]
_PARSER_ANALYSIS_TABLE['expressaoASgeral', '-'] = [ 'expressaoMDgeral', 'operacaoASgeral' ]
_PARSER_ANALYSIS_TABLE['expressaoASgeral', 'NROpositivo'] = [ 'expressaoMDgeral', 'operacaoASgeral' ]
_PARSER_ANALYSIS_TABLE['expressaoASgeral', 'CAC'] = [ 'expressaoMDgeral', 'operacaoASgeral' ]
_PARSER_ANALYSIS_TABLE['expressaoASgeral', 'caractere'] = [ 'expressaoMDgeral', 'operacaoASgeral' ]
_PARSER_ANALYSIS_TABLE['expressaoASgeral', '('] = [ 'expressaoMDgeral', 'operacaoASgeral' ]
_PARSER_ANALYSIS_TABLE['operacaoASgeral', '+'] = [ '+', 'expressaonumerica' ]
_PARSER_ANALYSIS_TABLE['operacaoASgeral', '-'] = [ '-', 'expressaonumerica' ]
_PARSER_ANALYSIS_TABLE['operacaoASgeral', '=='] = [ 'None' ]
_PARSER_ANALYSIS_TABLE['operacaoASgeral', '!='] = [ 'None' ]
_PARSER_ANALYSIS_TABLE['operacaoASgeral', '>'] = [ 'None' ]
_PARSER_ANALYSIS_TABLE['operacaoASgeral', '<'] = [ 'None' ]
_PARSER_ANALYSIS_TABLE['operacaoASgeral', '>='] = [ 'None' ]
_PARSER_ANALYSIS_TABLE['operacaoASgeral', '<='] = [ 'None' ]
_PARSER_ANALYSIS_TABLE['operacaoASgeral', '&&'] = [ 'None' ]
_PARSER_ANALYSIS_TABLE['operacaoASgeral', '||'] = [ 'None' ]
_PARSER_ANALYSIS_TABLE['operacaoASgeral', ','] = [ 'None' ]
_PARSER_ANALYSIS_TABLE['operacaoASgeral', ';'] = [ 'None' ]
_PARSER_ANALYSIS_TABLE['operacaoASgeral', ')'] = [ 'None' ]
_PARSER_ANALYSIS_TABLE['expressaoMDgeral', 'IDE'] = [ 'parcelageral', 'operacaoMDgeral' ]
_PARSER_ANALYSIS_TABLE['expressaoMDgeral', 'verdadeiro'] = [ 'parcelageral', 'operacaoMDgeral' ]
_PARSER_ANALYSIS_TABLE['expressaoMDgeral', 'falso'] = [ 'parcelageral', 'operacaoMDgeral' ]
_PARSER_ANALYSIS_TABLE['expressaoMDgeral', '-'] = [ 'parcelageral', 'operacaoMDgeral' ]
_PARSER_ANALYSIS_TABLE['expressaoMDgeral', 'NROpositivo'] = [ 'parcelageral', 'operacaoMDgeral' ]
_PARSER_ANALYSIS_TABLE['expressaoMDgeral', 'CAC'] = [ 'parcelageral', 'operacaoMDgeral' ]
_PARSER_ANALYSIS_TABLE['expressaoMDgeral', 'caractere'] = [ 'parcelageral', 'operacaoMDgeral' ]
_PARSER_ANALYSIS_TABLE['expressaoMDgeral', '('] = [ 'parcelageral', 'operacaoMDgeral' ]
_PARSER_ANALYSIS_TABLE['operacaoMDgeral', '*'] = [ '*', 'expressaoMD' ]
_PARSER_ANALYSIS_TABLE['operacaoMDgeral', '/'] = [ '/', 'expressaoMD' ]
_PARSER_ANALYSIS_TABLE['operacaoMDgeral', '+'] = [ 'None' ]
_PARSER_ANALYSIS_TABLE['operacaoMDgeral', '-'] = [ 'None' ]
_PARSER_ANALYSIS_TABLE['operacaoMDgeral', '=='] = [ 'None' ]
_PARSER_ANALYSIS_TABLE['operacaoMDgeral', '!='] = [ 'None' ]
_PARSER_ANALYSIS_TABLE['operacaoMDgeral', '>'] = [ 'None' ]
_PARSER_ANALYSIS_TABLE['operacaoMDgeral', '<'] = [ 'None' ]
_PARSER_ANALYSIS_TABLE['operacaoMDgeral', '>='] = [ 'None' ]
_PARSER_ANALYSIS_TABLE['operacaoMDgeral', '<='] = [ 'None' ]
_PARSER_ANALYSIS_TABLE['operacaoMDgeral', '&&'] = [ 'None' ]
_PARSER_ANALYSIS_TABLE['operacaoMDgeral', '||'] = [ 'None' ]
_PARSER_ANALYSIS_TABLE['operacaoMDgeral', ','] = [ 'None' ]
_PARSER_ANALYSIS_TABLE['operacaoMDgeral', ';'] = [ 'None' ]
_PARSER_ANALYSIS_TABLE['operacaoMDgeral', ')'] = [ 'None' ]
_PARSER_ANALYSIS_TABLE['parcelageral', 'IDE'] = [ 'IDEvetoroucompostoouchamada' ]
_PARSER_ANALYSIS_TABLE['parcelageral', 'verdadeiro'] = [ 'verdadeiro' ]
_PARSER_ANALYSIS_TABLE['parcelageral', 'falso'] = [ 'falso' ]
_PARSER_ANALYSIS_TABLE['parcelageral', '-'] = [ 'NRO' ]
_PARSER_ANALYSIS_TABLE['parcelageral', 'NROpositivo'] = [ 'NRO' ]
_PARSER_ANALYSIS_TABLE['parcelageral', 'CAC'] = [ 'CAC' ]
_PARSER_ANALYSIS_TABLE['parcelageral', 'caractere'] = [ 'caractere' ]
_PARSER_ANALYSIS_TABLE['parcelageral', '('] = [ '(', 'expressaogeral', ')' ]


PARSER_ANALYSIS_TABLE: MappingProxyType = MappingProxyType(_PARSER_ANALYSIS_TABLE)


DIFFERENT_TERMINAL: Final = 1
FAIL_ON_DERIVATIVE: Final = 2