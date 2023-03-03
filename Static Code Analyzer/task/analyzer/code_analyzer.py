import re
import sys
import os

file_paths = []
args = sys.argv
if ".py" in args[1]:
    file_path = args[1]
else:
    py_files = []
    for file in os.listdir(args[1]):
        if file.endswith(".py"):
            py_files.append(file)
    py_files = sorted(py_files)
    for file in py_files:
        file_path = f'{args[1]}\{file}'
        if 'tests.py' in file_path or '__init__.py' in file_path:
            continue
        file_paths.append(file_path)

cnt = 0


def too_long1(line):
    if len(line) > 79:
        print(f'{file_path}: Line {cnt}: S001 Too long')


def indentation_multiple_of_four2(line):
    if line.startswith(' ') and (not (re.match(r'\s{4}@?\w', line) or re.match(r'\s{8}\w', line))):
        print(f'{file_path}: Line {cnt}: S002 Indentation is not a multiple of four')


def unnecessary_semicolon3(line):
    if line.startswith('#'):
        pass
    elif re.match(r"(.+)('.+;')", line):
        pass
    elif re.match(r"(.+)(#.+;)", line):
        pass
    elif ';' in line:
        print(f'{file_path}: Line {cnt}: S003 Unnecessary semicolon')


def two_spaces4(line):
    if '#' in line and not line.startswith('#'):
        if not re.search(r'.+\s{2,}#', line):
            print(f'{file_path}: Line {cnt}: S004 At least two spaces required before inline comments')


def to_do5(line):
    if '#' in line:
        if re.match(r'.*todo.*', line, flags=re.IGNORECASE) and (not re.match(r"(.+)('todo')(.*)", line)):
            print(f'{file_path}: Line {cnt}: S005 TODO found')


def spaces_after_construction_name7(line):
    if 'def' in line:
        construction_name = 'def'
    else:
        construction_name = 'class'
    if 'def' in line or 'class' in line:
        if re.match(r'(\s+)?(def|class)(\s{2})', line):
            print(f"{file_path}: Line {cnt}: S007 Too many spaces after '{construction_name}'")


def class_name8(line):
    if 'class' in line:
        if not re.match(r'class\s+[A-Z]+[a-z]+', line):
            c_name = line[6:-2].rstrip()
            print(f"{file_path}: Line {cnt}: S008 Class name '{c_name}' should be written in CamelCase")


def f_name9(line):
    if 'def' in line:
        if 'def __init__' in line:
             pass
        elif not re.match(r'(\s+)?def\s+[a-z]+(_[a-z]+)?', line):
            d_name = line.lstrip()[3:-4].lstrip()
            print(f"{file_path}: Line {cnt}: S009 Function name '{d_name}' should use snake_case")


empty_lines = 0

if len(file_paths) > 0:
    for file_path in file_paths:
        cnt = 0
        empty_lines = 0
        with open(file_path, 'r') as file:
            lines = file.readlines()
            for line in lines:
                cnt += 1
                too_long1(line)
                indentation_multiple_of_four2(line)
                unnecessary_semicolon3(line)
                two_spaces4(line)
                to_do5(line)
                if line == "\n":
                    empty_lines += 1
                elif line != "\n":
                    if empty_lines > 2:
                        print(f'{file_path}: Line {cnt}: S006 More than two blank lines preceding a code line')
                        empty_lines = 0
                    else:
                        empty_lines = 0
                spaces_after_construction_name7(line)
                class_name8(line)
                f_name9(line)

else:
    if ".py" in args[1]:
        file_path = args[1]
        with open(file_path, 'r') as file:
            lines = file.readlines()
            for line in lines:
                cnt += 1
                too_long1(line)
                indentation_multiple_of_four2(line)
                unnecessary_semicolon3(line)
                two_spaces4(line)
                to_do5(line)
                if line == "\n":
                    empty_lines += 1
                elif line != "\n":
                    if empty_lines > 2:
                        print(f'{file_path}: Line {cnt}: S006 More than two blank lines preceding a code line')
                        empty_lines = 0
                    else:
                        empty_lines = 0
                spaces_after_construction_name7(line)
                class_name8(line)
                f_name9(line)
