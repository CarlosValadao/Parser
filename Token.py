from constants import TOKENS, UNKNOWN_TOKEN

class Token:
    # formated token deve vir no seguinte formato
    # numero_linha classe lexema
    def __init__(self, formated_token: str) -> None:
        splited_formated_token = formated_token.split(' ')
        self._line_number: int = int(splited_formated_token[0])
        self._token_type: str = splited_formated_token[1]
        self._lexeme: str = splited_formated_token[2]
        self.f_token: str = formated_token
    
    def get_token_type(self) -> str:
        return self._token_type

    def get_lexeme(self) -> str:
        return self._lexeme

    def get_line_number(self) -> int:
        return self._line_number
    
    def get_ftoken(self) -> str:
        return f'{self._line_number} {self._token_type} {self._lexeme}'
    
    def set_lexeme(self, lexeme:str) -> None:
        self._lexeme = lexeme
    