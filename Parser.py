import constants
from Stack import Stack
from types import MappingProxyType
from typing import TextIO
import Tools
from Token import Token


# Ha um hierarquia entre EOIF e EOF
# de tal forma que a hierarquia de EOIF e superior
# a de EOF, e apenas a funcao de setar um novo arquivo
# de entrada e capaz de modificar EOIF, enquanto as funcoes
# que leem o arquivo atual sao apenas capazes de modificar EOF
# e trabalham sobre o arquivo de entrada atual, representado pela
# seguinte expressao: self.input_file = self.input_files[self.file_counter]
class Parser:
    # O boçal deve fornecer uma lista nao vazia de arquivos de entrada
    # caso contrario o algoritmo todo vai quebrar
    def __init__(self, start_symbol:str, input_files: tuple[str]) -> None:
        self.n_input_files: int = len(input_files)
        # End Of Input Files
        self.EOIF = False
        self._start_symbol: str = start_symbol
        self.input_files: tuple[str] = input_files
        self.file_counter: int = 0
        self._input_file: TextIO = open(input_files[self.file_counter], 'r')
        self.file_counter += 1
        # se preocupar com o fim dos arquivos de entrada
        # algo como EOIF -> End Of Input Files
        self._table: MappingProxyType = constants.PARSER_ANALYSIS_TABLE
        # self._stack: list[str] = ['$', start_symbol]
        self.stack: Stack = Stack()
        self.stack.pushl(['$', self._start_symbol])
        # self.mantaining: bool = True
        self.EOF: bool = Tools.is_empty_text_file(self._input_file.fileno())
        # self.is_empty_file: bool = False
        self._token:Token = self.get_next_token()
        # Guarda as mensagens de erro, de acordo com
        # a execucao do programa
        self._error_messages: list[str] = []
        self._messages: dict[str, list[str]] = dict()
        # self.derivative()
    
    # Defini um novo arquivo a ser analisado, entao todas
    # as configuracoes (variaveis) do objeto devem
    # ser devidamente resetadas
    def _set_new_current_input_file(self) -> None:
        if 0 < self.file_counter < self.n_input_files:
            # self.handle_output()
            self._error_messages.clear()
            self.stack.clear()
            self.stack.pushl([ '$', self._start_symbol ])
            self._input_file = open(self.input_files[self.file_counter], 'r')
            self.file_counter += 1
            self.EOF = Tools.is_empty_text_file(self._input_file.fileno())
            self._token = self.get_next_token()
            # self._error_messages.clear()
        else:
            self.EOIF = True
    
    def _write_in_output_file(self, suffix: str) -> None:
        # output_filename = self.input_filename + suffix
        # fp = open(output_filename, 'w')
        # fp.writelines(self._error_messages)
        # ESCRITA QUE DEVE SER FEITA NO ARQUIVO DE SAIDA
        # fp.close()
        return
    
    def _write_output_file(self) -> None:
        return
    
    # def test_read_all(self, input_files: list[str]) -> None:
    #     self.run()
    #     print("PASSOU")
    #     print(self._error_messages)
    #     for file in input_files:
    #         self._set_new_current_input_file(file)
    #     # self.read_all_the_file()
    #     self.run()

    def testar_conversao_tokens(self) -> None:
        print(self._token.get_ftoken())
        while not self.EOF:
            self._token = self.get_next_token()
            print(self._token.get_ftoken())
            
    
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
            # Caraceteres diferentes (Caso de Erro)
            # Aqui a recuperacao de erro deve ser invocada, para sanar
            # e as devidas flagas de erro devem ser setadas
            else:
                print('ENTRADA REJEITADA PELA LINGUAGEM')
                # print("PILHA ->", self.stack.get_content())
                # print("TABLEA AS -> ", self._table)
                print("AQUI NO ERRO DE TOKENS DIFERENTES")
                expected_token = self.stack.peek()
                print("TOKEN ESPERADO ->", expected_token)
                print("TOKEN DO TOPO DA PILHA ->", self.stack.peek())
                print("TOKEN ATUAL ->", self._token.get_lexeme())
                print("SAINDO...")
                print(f"ERA ESPERADO O TERMINAL {expected_token}, mas {self._token.get_lexeme()}\n \
                      FOI FORNECIDO")
                # exit()
                self.handle_error_messages(self._token.get_line_number(),
                                                            (expected_token,), self._token.get_lexeme())
                # exit()
                # self.error_recovery(expected_token)
                # self.EOF = True
                # self.stack.clear()
                self.recover_unexpected_terminal_error()
                return
        else:
            self.derivative()
    
    def run(self) -> None:
        while not self.EOIF:
            self.derivative()
            while not self.EOF or not self.stack.is_empty():
                if self.EOF and not self.stack.is_empty():
                    break
                self.step_away()
            self._set_new_current_input_file()
            self._messages[self.input_files[self.file_counter-1]] = self._error_messages
            self.handle_output()
        print("MENSAGENS DE ERRO ->", self._messages)
        print(self.input_files)
        
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
        # Producao que nao existe
        if not productions:
            print("Algo deu errado com a producao")
            expected_tokens = self.handle_unexpected_token(constants.FAIL_ON_DERIVATIVE, variable)
            print(f"ERAM ESPERADOS {expected_tokens}")
            print(f"AO INVES DE {self._token.get_lexeme()}")
            print(f'REGRA ->', variable)
            self.handle_error_messages(self._token.get_line_number(), expected_tokens,
                                       terminal)
            # self.stack.clear()
            # exit()
            self.recover_inexistent_production(expected_tokens)
            self.stack.push(variable)
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
            token = Token(line)
            # print("LEXEMA TOKEN LIDO ->", token.get_lexeme())
            if token.get_lexeme() == 'funcao':
                token = self.get_next_token()
                print("TOKEN LIDO ->", token.get_lexeme())
                # exit(0)
            # Verificar se a alteracao e por referencia
            self.replace_some_lexemes(token)
            return token
        else:
            raise Exception("Arquivo Vazio, como entrada")

    # Substitui alguns lexemas de determinados
    # tokens com base em uma lista, para atender
    # a alguns requisitos da gramatica
    def replace_some_lexemes(self, token: Token) -> None:
        token_type = token.get_token_type()
        if token_type in constants.KEYS_SPECIAL_TYPES:
            token.set_lexeme(constants.SPECIAL_TYPES[token_type])
            
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
    def handle_unexpected_token(self, error_type: int, var: str) -> tuple[str]:
        if error_type == constants.DIFFERENT_TERMINAL:
            terminal = self.stack.peek()
            return ( terminal, )
        else:
            # var = self.stack.peek()
            var_produtcions = Tools.values_with_key_substring(self._table, var)
            return var_produtcions
    
    # Responsavel por se recuperar de um erro, caso
    # um token inesperado seja encontrado
    # next_tokens e uma lista que contem os prixmos
    # possiveis lexemas para que seja possivel uma recuperacao
    # de erro
    # O algoritmo ira consumir os tokens ou ate chegar ao final
    # do arquivo ou ate encontrar o token esperado ou
    # um dos tokens esperados
    
    def recover_inexistent_production(self, next_tokens: tuple[str]) -> None:
        # Caso mais simples: Um unico token e esperado
        # dentre os possiveis tokens
        while not self.EOF:
            self._token = self.get_next_token()
            if self._token.get_lexeme() in next_tokens:
                return
    
    # Essa funcao e responsavel por fornecer ao algoritmo de analise sintatica o token
    # esperado, em caso de ocorrer um erro na analise sintatica
    def recover_unexpected_terminal_error(self) -> None:
        while not self.EOF:
            self._token = self.get_next_token()
            if self._token.get_lexeme() == self.stack.peek():
                print("\n\nENCONTROU O TOKEN ESPERADO!")
                return
        
    # generate error formated string
    # gerar string de erro formatada
    def generate_error_fstring(self, line: int, expected_terminals: tuple[str], found_terminal: str) -> str:
        return f'Na linha {line} esperava-se {expected_terminals} e fora encontrado {found_terminal}\n'
    
    def handle_error_messages(self, line: int, expected_terminals: tuple[str], found_terminal: str) -> None:
        error_message = self.generate_error_fstring(line,
                                                    expected_terminals, found_terminal)
        self._error_messages.append(error_message)
    
    # Responsavel por formatar as mensagens
    # para que estejam de acordo coma saida
    # resultante exigida pelo problema
    def handle_output(self) -> None:
        for key, value in self._messages.items():
            has_no_error_messages = len(value) == 0
            if has_no_error_messages:
                self._messages[key].append('\nENTRADA ACEITA PELA LINGUAGEM\n')
            else:
                init_error_message = "\n\t A ENTRADA FOI REJEITADA PELA LINGUAGEM, POIS:\n"
                self._messages[key].insert(0, init_error_message)
                
    def get_output(self) -> dict[str, list[str]]:
        return self._messages