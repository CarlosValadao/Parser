import constants
from sys import exit
from os import path, listdir, mkdir, chdir, rename, remove, path
from typing import Iterable
from types import MappingProxyType

_EXIT_FAILURE = 1
_EXIT_SUCCESS = 0

def identify_token(token:str) -> str:
    id_token = token in constants.TOKENS
    return token if id_token else constants.UNKNOWN_TOKEN

# Get all of the files that ends with .txt
def get_input_filenames(not_endswith: str, rpath:str = '.') -> tuple[str]:
    filenames = listdir(rpath)
    size_not_endswith = len(not_endswith) + 4
    not_endswith = f'{not_endswith}.txt'
    is_text_file = lambda filename: filename[-size_not_endswith:] != not_endswith
    input_filenames = tuple(filter(is_text_file, filenames))
    return input_filenames

def generate_output_filenames(filenames: tuple[str]|str, sufix: str) -> tuple[str]:
    rename_file = lambda filename: filename[0:-4] + f'{sufix}.txt'
    output_filenames = tuple(map(rename_file, filenames))
    return output_filenames

def dir_exists(dir_path:str) -> bool:
    exists = path.exists(path=dir_path)
    if exists:
        return True
    else:
        print(f'Diretório "{dir_path}" inexistente!')
        exit(_EXIT_FAILURE)

def _change_work_dir(work_path:str) -> bool:
    try:
        chdir(work_path)
        return True
    except PermissionError as ex:
        print(f'Você não possui permissão para acessar "{work_path}"')
        exit(_EXIT_FAILURE)

def change_dir(path:str) -> None:
    if dir_exists(dir_path=path):
        has_success_on_change_dir = _change_work_dir(path)
        if not has_success_on_change_dir:
            exit(_EXIT_FAILURE)
        
def is_empty_text_file(fd: int) -> bool:
    is_empty = not bool(path.getsize(fd))
    return is_empty


def endswithnewline(obj: list[str]) -> bool:
    ends = True if obj[-1] == '\n' else False
    return ends

# Recebe um dicionario e verifica
# e retorna as chaves do dicionário
# que contém value, em forma de tupla
def values_with_key_substring(dictionary: MappingProxyType, value: str) -> tuple[str]:
    return tuple([ key[1] for key in dictionary if value in key ])

def write_file(fpath: str, data: list[list[str]], mode: str) -> None:
    lines = [ line for tokens in data for line in tokens ] 
    fp = open(fpath, mode)
    fp.writelines(lines)
    fp.close()

def write_files(f_paths: tuple[str], data: list[list[list[str]]], mode: str) -> None:
    for i in range(len(f_paths)):
        write_file(f_paths[i], data[i], mode)

# renomeia um arquivo ou um conjunto de arquivos
# levando em consideracao o diretorio de trabalho atual, apenas
# claro, ambas as listas devem ter o mesmo tamanho
# nao faz verificacao de erro
def rename_files(old: list[str], new: list[str]) -> None:
    for k in range(len(old)):
        if old[k] != new[k]:
            rename(old[k], new[k])
    # genexp
    # (rename(old_item, new_item) for old_item, new_item in zip(old, new))
    
def remove_files(files: tuple[str]) -> None:
    
    for file in files:
        if path.exists(file):
            remove(file)
        else:
            print("Não existem arquivos de saída!")
            return
