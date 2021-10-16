from typing import Pattern
import pandas as pd
import os
from os import read, walk
from os.path import exists as file_exists
import shutil
import re
import fop

def parse_monitor_record(value):
    """Converts values like +5 into 1, -5 into 0"""
    if type(value) == str and "+" in value:
        return 1
    if type(value) == str and "-" in value:
        return 0
    return value


def change_names(name):
    """Removes patronymic and replaces ё with e"""
    name = name.replace("ё", "e")
    splitted = name.split()
    try:
        return " ".join(splitted[:2])
    except:
        return name


def generate_standings_filename(contest_number: int) -> str:
    """Generates a filename for a file with contest results by contest number"""
    return f"standings_{contest_number}.csv"


def check_bullshit(contest_number: int):
    df = pd.read_csv(generate_standings_filename(contest_number), index_col=1)
    df = df.iloc[:, 2:-2]
    df.fillna(value=0, inplace=True)
    df = df.applymap(parse_monitor_record)

    df.index = map(change_names, df.index)

    names = pd.read_csv("students_names.csv").set_index("user_name")
    df = df.join(names, how="right").sort_index().fillna(0)

    df.columns = [i + 1 for i in range(len(df.columns))]

    filename = f"results_{contest_number}.xlsx"
    df.to_excel(filename)
    print(f"Wrote results into {filename}")


def read_contest_number() -> int:
    n = "This\ncannot\tbe{filename}\n\n"

    while not file_exists(generate_standings_filename(n)):
        n = int(input("Insert the number of contest file (contest_<num>.csv): "))

    return n

def check_student_names_file_exists():
    if not file_exists("student_names.csv"):
        raise Exception("File with student names (student_names.csv) is not found!")


def get_solutions(path):
    files = []
    for folder in os.scandir(path):
        if folder.is_dir():
            for filez in os.scandir(folder.path):
                if filez.is_file() and filez.path.endswith('.py'):
                    files += [filez.path]
    return files


def copy_solution(where_from, where_to):
    '''check this method'''
    shutil.copy(where_from, where_to)

def create_empty_dir(dir_to_copy):
    try:
        os.rmdir(dir_to_copy) 
    except:
        pass
    os.makedirs(dir_to_copy, exist_ok=True)

def chech_forbiden_methods(dir_name = "/Users/fuckingbell/Downloads/submits", *args):
    """trying to put solution under suspicion into new folder"""
    pass


def get_student_name(current_dir):
    pat = r".+/((.+ .+ .+)|(.+ .+))-"
    match = re.match(pat, current_dir[30:])
    return match.group(1)

def kirill_func(path, *args):
    dir_to_copy = os.path.join(os.getcwd(), "copied_files")
    create_empty_dir(dir_to_copy)

    for current_dir, dirs, files in os.walk(path):
        if current_dir != path:
            student_name = get_student_name(current_dir)

            for file in files:
                if file != ".DS_Store" and "OK.py" in file:
                    path_to_solution = os.path.join(dir_to_copy, current_dir, file)
                    found_tokens = fop.check_out_tokens(path_to_solution, *args)

                    if found_tokens:    
                        fop.copy_solution(path_to_solution, student_name, file)

if __name__ == "__main__":
    # dir_name = input("enter archive dir: ")
    # tokens = input("enter tokens: ").split()


    path = "/Users/fuckingbell/Downloads/submits"

    # kirill_func(path, "if")

    # dir = "/Users/fuckingbell/Downloads/submits/Шингирий Павел Викторович-92574401"


    for current_dir, dirs, files in os.walk(path):
        # if current_dir != path:
        #     pat = r".+/((.+ .+ .+)|(.+ .+))-"
        #     match = re.match(pat, current_dir[30:])
        #     if match== None:
        #         print(current_dir)
        #     else:
        #         print(match.group(1))


                # with open(path_to_solution, "r+", encoding='utf-8') as solution:
                #     code = solution.read()
                #     print(code)
                #     found_tokens = []
                #     for token in args:

                #         pattern = r"{}".format(f"({token})")
                #         match = re.findall(pattern, code)
                #         print(match)
                #         if len(match) > 0:
                #             found_tokens.append(token)
                        
                        #I can add commets which particullar tokens have been found"""