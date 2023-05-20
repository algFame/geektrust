import os
from sys import argv

from src.rider_sharing import *

import sys
from io import StringIO

from diff_match_patch import diff_match_patch
from colorama import Fore, Style

def highlight_differences(text1, text2):
    dmp = diff_match_patch()
    diffs = dmp.diff_main(text1, text2)
    dmp.diff_cleanupSemantic(diffs)

    highlighted_diff = ""
    for diff in diffs:
        if diff[0] == -1:
            highlighted_diff += Fore.RED + diff[1] + Style.RESET_ALL
        elif diff[0] == 1:
            highlighted_diff += Fore.GREEN + diff[1] + Style.RESET_ALL
        else:
            highlighted_diff += diff[1]

    return highlighted_diff

def capture_output(func,*args,**kwargs):
    output = StringIO()
    sys.stdout = output

    func(*args,**kwargs)

    sys.stdout = sys.__stdout__

    return output.getvalue()

def compare_output(output_value, expected_output_file)->bool:
    with open(expected_output_file, 'r') as f:
        expected_output = f.read().strip()

    output_value = output_value.strip()

    if output_value != expected_output:
        print("Output does not match the expected output.")
        print()
        highlighted_diff = highlight_differences(expected_output, output_value)
        print(highlighted_diff)
        print()

    return output_value == expected_output

def main():
    """
    Sample code to read inputs from the file

    if len(argv) != 2:
        raise Exception("File path not entered")
    file_path = argv[1]
    f = open(file_path, 'r')
    Lines = f.readlines()
    //Add your code here to process the input commands
    """
    test_folder = "sample_input"


    if len(argv) != 2:
        # argv.append(os.path.join(test_folder, input_file))
        for i in os.listdir(test_folder):
            if i.endswith(".txt") and i.startswith("input"):
                argv.append(os.path.join(test_folder, i))


    for file_path in argv[1:]:
        print("testcase-",file_path)
        print()
        input_file = os.path.split(file_path)[1]


        f = open(file_path, 'r')
        testcase = [i.strip() for i in f.readlines() if len(i) > 0]
        f.close()

        output = StringIO()

        for i in testcase:
            ic(i)
            sys.stdout = output

            command_parser(i)

        sys.stdout = sys.__stdout__

        print(output.getvalue())

        cmp_output = compare_output(output.getvalue(), os.path.join(test_folder, input_file.replace("input", "output")))

        if cmp_output:
            print("Testcase passed")
        else:
            print("Testcase failed")
            print()
            sys.exit(1)

        print()

if __name__ == "__main__":
    if os.getenv("mode") != "dev":
        ic.disable()
    main()
