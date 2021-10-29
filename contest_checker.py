from typing import Pattern, List
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


def marks_to_xlsx(contest_number: int):
    """truns students' standings into a xlsx table"""
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
    '''input contest number'''
    n = "This\ncannot\tbe{filename}\n\n"

    while not file_exists(generate_standings_filename(n)):
        n = int(input("Insert the number of contest file (contest_<num>.csv): "))
    return n


def check_student_names_file_exists():
    if not file_exists("student_names.csv"):
        raise Exception(
            "File with student names (student_names.csv) is not found!")


def create_empty_dir(dir_to_copy):
    '''creates empty dir to copy solutions in'''
    try:
        os.rmdir(dir_to_copy)
    except:
        pass
    os.makedirs(dir_to_copy, exist_ok=True)


def get_student_name(current_dir):
    '''extract student name surname from dir'''
    pat = r".+/(.+ .+[ .]*)-"
    match = re.match(pat, current_dir[30:])
    try:
        return match.group(1)
    except:
        print("problem with " + current_dir)


def check_files(path, tokens: List[str]):
    """main func. It goes through all the solutions to find those with forbiden methods"""
    dir_to_copy = os.path.join(os.getcwd(), "copied_files")
    create_empty_dir(dir_to_copy)

    for current_dir, dirs, files in os.walk(path):
        if current_dir != path:
            student_name = get_student_name(current_dir)

            for file in files:
                if file != ".DS_Store" and "OK.py" in file:
                    path_to_solution = os.path.join(
                        dir_to_copy, current_dir, file)
                    found_tokens = fop.check_out_tokens(
                        path_to_solution, tokens)

                    if found_tokens:
                        fop.copy_solution(path_to_solution, student_name)

    print(f'all the solutions have been checked')


def define_mode():
    """input a working mode"""
    mode_index = input("Enter the number of the mode you want to work in: "
                       "\n1 — transfer marks to excel;"
                       "\n2 — find all solutions with forbiden methods in.\n").strip()

    if mode_index not in ('1', '2', '3'):
        while True:
            mode_index = input("Enter the number of the mode you want to work in: "
                               "\n1 — transfer marks to excel;"
                               "\n2 — find all solutions with forbiden methods in.\n").strip()
            if mode_index in ('1', '2'):
                break
    return ("transfer", "find")[int(mode_index) - 1]


def robocop():
    default_path = "/Users/fuckingbell/Downloads/submits"
    archive_path = input("enter dir the solutions archive:"
                         f"\n'default' will use {default_path} "
                         "as a path.\n").strip()
    
    if archive_path == "default":
        archive_path = default_path
    tokens = list(input("enter the list tokens using spaces: ").split())

    check_files(path, tokens)


def opperate(mode):
    if mode == "transfer":
        marks_to_xlsx()
    else:
        robocop()


if __name__ == "__main__":
    # marks_to_xlsx()
    opperate(define_mode())
