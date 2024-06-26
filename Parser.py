import constants
from Stack import Stack
from types import MappingProxyType
from typing import TextIO
import Tools
from Token import Token

class Parser:
    def __init__(self, start_symbol:str, input_file: str) -> None:
        self._start_symbol: str = start_symbol
        self._input_file: TextIO = open(input_file, 'r')
        self._table: MappingProxyType = constants.PARSER_ANALYSIS_TABLE
        # self._stack: list[str] = ['$', start_symbol]
        self.stack: Stack = Stack()
        self.stack.pushl(['$', self._start_symbol])
        # self.mantaining: bool = True
        self.EOF: bool = Tools.is_empty_text_file(self._input_file.fileno())
        # self.is_empty_file: bool = False
        self._token:Token = self.get_next_token()
        # self.derivative()
    
    # Defini um novo arquivo a ser analisado, entao todas
    # as configuracoes (variaveis) do objeto devem
    # ser devidamente resetadas
    def _set_new_current_input_file(self, input_file:str) -> None:
        self.stack.clear()
        self.stack.pushl([ '$', self._start_symbol ])
        self._input_file = open(input_file, 'r')
        self.EOF = Tools.is_empty_text_file(self._input_file.fileno())
        self._token = self.get_next_token()
        return
    
    def _write_on_output_file(self) -> None:
        print("ESCREVENDO NO RESPECTIVO ARQUIVO DE SAÍDA")
        return
    
    def test_read_all(self, input_files: list[str]) -> None:
        self.run()
        print("PASSOU")
        for file in input_files:
            self._set_new_current_input_file(file)
        # self.read_all_the_file()
        self.run()
    
    # Verifica se o que esta no topo da pilha
    # e um terminal ou nao
    def is_terminal(self) -> bool:
        # return True if self._stack[-1] in constants.TERMINALS else False
        return True if self.stack.peek() in constants.TERMINALS else False
    
    # Verifica se o que esta no topo da pilha
    # e um terminal ou nao
    def is_non_terminal(self) -> bool:
        return not self.is_terminal()
    
    # def set_input(self, input: str) -> None:
    #     self._entrada = input + '$'
    #     self._input_pointer = 0
    
    # Faz a analise sintatica e retorna
    # true caso a entrada foi aceita
    # e false caso contrario
    def step_away(self) -> None:
        print("PILHA -> ", self.stack.get_content())
        print("LEXEMA -> ", self._token.get_lexeme())
        print("NUMERO LINHA -> ", self._token.get_line_number())
        # print(self.stack.get_content())
        if self.stack.peek() == '$' and self._token._lexeme == '$':
            print("ENTRADA ACEITA :D")
            self.EOF = True
            self.stack.pop()
            return
        if self.is_terminal():
            # if self._entrada[self._input_pointer] == self._stack[-1]:
            if self.stack.peek() == self._token.get_lexeme():
                self._token = self.get_next_token()
                self.stack.pop()
            else:
                print('ENTRADA REJEITADA PELA LINGUAGEM')
                # print("PILHA ->", self.stack.get_content())
                # print("TABLEA AS -> ", self._table)
                expected_token = self.handle_unexpected_token(constants.DIFFERENT_TERMINAL)
                print(f"ERA ESPERADO O TERMINAL {expected_token}, mas {self._token.get_lexeme()}\n \
                      FOI FORNECIDO")
                self.EOF = True
                self.stack.clear()
                return
        else:
            self.derivative()
    
    def run(self) -> None:
        self.derivative()
        while not self.EOF or not self.stack.is_empty():
            self.step_away()
                         
    # Faz a derivacao da regra de producao
    # que se encontra no topo da pilha
    # e adiciona o conteudo da variavel
    # na pilha
    def derivative(self) -> None:
        print(self.stack.get_content())
        # nesse ponto nao ha como existir
        # erros ao recuperar o dado, pois
        # uma outra verificacao e feita antes
        # da chamada dessa funcao
        variable = self.stack.pop()
        terminal = self._token.get_lexeme()
        productions: list[str] = self._table.get((variable, terminal), [])
        if not productions:
            print("Algo deu errado com a producao")
            expected_tokens = self.handle_unexpected_token(constants.FAIL_ON_DERIVATIVE)
            print(f"ERAM ESPERADOS {expected_tokens}")
            print(f"AO INVES DE {self._token.get_lexeme()}")
            self.stack.clear()
            return
        if productions[0] == 'None':
            return
        cpy_productions = productions.copy()
        cpy_productions.reverse()
        print("DERIVANDO -> ", productions)
        self.stack.pushl(cpy_productions)
        print("DEPOIS DE DERIVAR -> ", self.stack.get_content())

    def get_next_text_file_line(self) -> str:
        if self.EOF:
            return ''
        else:
            line = self._input_file.readline().strip('\n')
            if line == constants.EOI_RIGHT_TOKENS_NO_NEWLINE:
                self._input_file.close()
                self.EOF = True
                return line
            else:
                return line
    
    def get_next_token(self) -> Token:
        line = self.get_next_text_file_line()
        if line != '':
            return Token(line)
        else:
            raise Exception("Arquivo Vazio, como entrada")
            
    # A depender do valor de uma variavel
    # esta funcao vai retornar ou o lexema do
    # token ou a classe do token (tipo do token)
    def handle_token(self) -> None:
        return

    def read_all_the_file(self) -> None:
        print("LENDO ARQUIVO _>\n")
        print(self._token.get_ftoken())
        while not self.EOF:
            print(self.get_next_text_file_line())

    # Essa funcao vai lidar com os possiveis
    # erros
    # (1) -> Erro ao comparar dois terminais, e estes
    # são diferentes um do outro
    # (2) -> Erro de produzir algo que é impossível de
    # produzir de acordo com a gramática
    # Error type pode ser (1) ou (2)
    # Devolve o token esperado ou os possíveis tokens esperados
    # na forma de lista de string
    def handle_unexpected_token(self, error_type: int) -> list[str]:
        if error_type == constants.DIFFERENT_TERMINAL:
            terminal = self.stack.peek()
            return [ terminal ]
        else:
            var = self.stack.peek()
            var_produtcions = Tools.values_with_key_substring(self._table, var)
            return var_produtcions
    