# Pilha "tipada" que armazena apenas
# strings (str)
class Stack:
    def __init__(self) -> None:
        self.stack: list[str] = []
    
    def push(self, value: str) -> None:
        self.stack.append(value)

    # pushl vem de push list
    def pushl(self, value: list[str]) -> None:
        self.stack.extend(value)

    def is_empty(self) -> bool:
        return len(self.stack) == 0
    
    def pop(self) -> str:
        if self.is_empty():
            raise IndexError("pop from empty stack")
        else:
            return self.stack.pop()
    
    def peek(self) -> str:
        if self.is_empty():
            raise IndexError("peek from empty stack")
        else:
            return self.stack[-1]
    
    def size(self) -> int:
        return len(self.stack)

    def clear(self) -> None:
        if not self.is_empty():
           return self.stack.clear() 
    
    def get_content(self) -> list[str]:
        return self.stack
    
    