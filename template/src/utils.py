
import sys
from io import StringIO

from diff_match_patch import diff_match_patch
from colorama import Fore, Style

import re
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

def capture_output(func,*args,**kwargs)->str:
    output = StringIO()
    sys.stdout = output

    func(*args,**kwargs)

    sys.stdout = sys.__stdout__

    return output.getvalue()


def compare_output(output_value, expected_output_file)->bool:
    with open(expected_output_file, 'r') as f:
        expected_output = f.read().strip()

    output_value = output_value.strip()

    output_value = re.sub(r"ic\|.*\n", "", output_value)

    if output_value != expected_output:
        print("Output does not match the expected output.")
        print()
        highlighted_diff = highlight_differences(expected_output, output_value)
        print(highlighted_diff)
        print()

    return output_value == expected_output

