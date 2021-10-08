from os import read
import pandas as pd
from os.path import exists as file_exists


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

if __name__ == "__main__":
    contest_number = read_contest_number()
    check_bullshit(contest_number)
