
from LexcialScanner import LexcialScanner
from os import chdir, path, listdir, sep, mkdir
import Tools
from Parser import Parser
from time import sleep

# negrito = "\033[1m"
# reset = "\033[0m"
# get_directories = lambda file: path.isdir(file)
# working_dir_files = listdir(path.abspath('.'))
# dirs = list(filter(get_directories, working_dir_files))
# files_path = path.abspath('.') + sep + 'files'
# if not 'files' in dirs:
#     print(negrito + 'Por favor, crie uma pasta chamada "files" na raiz do projeto\n \
#         (1) E adicione os seus arquivos de entrada\n\
#          (2) Quaislquer dúvidas leia README.txt ou então execute\n\
#                 python main.py -h' + reset)
#     exit(1)
# chdir(files_path)

# parser = cli_parser()
# inputfiles = parser['infiles']
# outputflies = parser['outputfiles']

# get_filename = lambda file: file.split(sep)[-1]

# input_filenames = list(map(get_filename, inputfiles))
# output_filenames = list(map(get_filename, outputflies)) if outputflies != None else None

WORK_DIR = './files'
LEXICAL_SCANNER_FILES_SUFFIX = '-lexico-temp'
PARSER_FILES_SUFFIX = '-saida'
START_SYMBOL = 'algoritmov'
# PARSER_FILES_SUFFIX = LEXICAL_SCANNER_FILES_SUFFIX

Tools.change_dir(path=WORK_DIR)
input_filenames = Tools.get_input_filenames(PARSER_FILES_SUFFIX)
output_lexico_filenames = Tools.generate_output_filenames(input_filenames, LEXICAL_SCANNER_FILES_SUFFIX)
output_parser_filenames = Tools.generate_output_filenames(input_filenames, PARSER_FILES_SUFFIX)
# input_filenames = ['input.txt']
# output_filenames = None
if input_filenames:
    # Tools.remove_files(output_parser_filenames)
    # print(input_filenames)
    print("ARQUIVOS DE SAIDA DO LEXICO ->", output_lexico_filenames)
    print("ARQUIVOS DE SAIDA DO PARSER ->", output_parser_filenames)
    # exit()
    Tools.remove_files(output_parser_filenames)
    # Tools.remove_files(output_parser_filenames)
    # input("<ENTER>")
    #sleep(5.0)
    scanner = LexcialScanner(infiles=input_filenames)
    scanner.run()
    input_files_tokens = scanner.get_tokens()
    Tools.write_files(output_lexico_filenames, list(input_files_tokens.values()), mode='w')
    # parser = Parser(START_SYMBOL, ( 'id-s-lexico-temp.txt', ))
    parser = Parser(START_SYMBOL, output_lexico_filenames)
    parser.run()
    out = parser.get_output()
    print("SAIDA DO ANALISADOR SINTATICO ->", out)
    Tools.write_files(output_lexico_filenames, [ list(out.values()) ], mode='a')
    Tools.rename_files(list(output_lexico_filenames), list(output_parser_filenames))
    #Tools.write_files(output_parser_filenames, list(input_files_tokens.values()))
    # parser.run()
    # print("EM MAIN ->", list(input_files_tokens.kekys()))
    # scanner.exec(input_filenames[1:], output_filenames[1:])
    # scanner.load_files(input_filenames[1:], output_filenames[1:])    
    # scanner.run()
    # # # for i in range(l
    # en(input_filenames)):
    #     # out = output_filenames[i] if output_filenames != None else None
    #     scanner = LexcialScanner(infiles=[input_filenames[i]], outfiles=output_filenames)
    #     scanner._run()