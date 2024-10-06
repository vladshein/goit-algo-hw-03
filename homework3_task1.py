#Homework3 task1
'''
Напишіть програму на Python, яка рекурсивно копіює файли у вихідній директорії,
переміщає їх до нової директорії та сортує в піддиректорії, назви яких 
базуються на розширенні файлів.
'''

from pathlib import Path
from random import randint, choice, choices
from sys import argv, platform
from shutil import copy

def check_file_extension(file_name):
    file_path = Path(file_name)
    extension = file_path.suffix
    print(f"File extension: {extension}")
    extension_without_dot = extension[1:]
    return extension_without_dot


def create_folder_by_extention(output_folder, extension):
    folder_path = output_folder / extension
    folder_path.mkdir(parents=True, exist_ok=True)
    return folder_path

    
def parse_folder(input_folder, output_folder):
    for element in input_folder.iterdir():
        if element.is_dir():
            print(f"Parse folder: This is folder - {element.name}")
            parse_folder(element, output_folder)

        if element.is_file():
            print(f"Parse folder: This is file - {element.name}")
            extention = check_file_extension(element)
            print(extention)
            
            create_folder_by_extention(output_folder, extention)
            source = Path(element)
            print(f"Source is {source}")
            target = create_folder_by_extention(output_folder, extention)
            print(f"Target is {target}")
            try:
                copy(source, target)
            except Exception as e:
                print(e)
            


def parse_folder_recursion(path):
    for elements in path.iterdir():
        if elements.is_dir():
            parse_folder_recursion(elements)

def create_target_folder(dir_path):
    dir_path.mkdir(parents=True, exist_ok=True)
    

def check_and_parse_arguments(args):
    argv_len = len(args)
    if argv_len not in [2,3]:
        raise ValueError("The number of arguments must be 2 or 3")
    
    if argv_len == 2:
        script, input_folder = args
        output_folder = "dist"
    else:
        script, input_folder, output_folder = args

    print("Script", script)
    print(f"Input folder is: {input_folder}")
    print(f"Output folder is: {output_folder}")

    return input_folder, output_folder


def main(args):
    #get, check and parse arguments
    input_folder = ""
    output_folder = ""
    try:
        input_folder, output_folder = check_and_parse_arguments(args)
    except Exception as e:
        print(e)
        exit(1)
        
    input_folder_path = Path(input_folder)
    output_folder_path = Path(output_folder)
    absolute_output_path = output_folder_path.resolve()

    create_target_folder(absolute_output_path)
    parse_folder(input_folder_path, absolute_output_path)
    

if __name__ == '__main__':
    main(argv)


