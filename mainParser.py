from Parser import Parser
import Tools

Tools.change_dir('./files')

# Existe algum erro na funcao derivative, na hora
# de remover da pilha, esta como se ela estivesse
# vazia, mas ela nao esta

parser = Parser('S', 'id-s-lexico-temp.txt')
# parser.read_all_file()
# parser.run()
parser.test_read_all(['id-s-lexico-temp-1.txt'])