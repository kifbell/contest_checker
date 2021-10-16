import os 
import shutil
import re


def copy_file(where_from, where_to):
    '''check this method'''
    shutil.copy(where_from, where_to)

def copy_solution(path_to_solution, student_name, solution):
    # where_from = os.path.join(dir_to_copy, current_dir, solution)
    where_to = os.path.join(os.getcwd(), "copied_files", f"{student_name}.py")
    # print(where_to)
    copy_file(path_to_solution, where_to)

def check_out_tokens(path_to_solution, *args):
    tokens = set
    with open(path_to_solution, "r+", encoding='utf-8') as solution:
        code = solution.read()
        found_tokens = []
        for token in args:

            pattern = r"{}".format(f"({token})")
            match = re.findall(pattern, code)
            # print(match)
            if len(match) > 0:
                found_tokens.append(token)
    return tokens

__all__ = ["copycopy_solution_file", "check_out_tokens"]

if __name__ == "__main__":
    pass