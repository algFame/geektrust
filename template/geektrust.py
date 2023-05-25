import os
import sys
from sys import argv

from icecream import ic

from src.testcase import run_testcase
from src.utils import compare_output, capture_output


def main():
    test_folder = "sample_input"
    test_specified = len(argv) == 2

    if not test_specified:
        for filename in os.listdir(test_folder):
            if filename.endswith(".txt") and filename.startswith("input"):
                argv.append(os.path.join(test_folder, filename))

    for file_path in sorted(argv[1:]):
        input_file = os.path.split(file_path)[1]

        with open(file_path, 'r') as f:
            testcase = [line.strip() for line in f if len(line.strip()) > 0]

        if test_specified:
            ic(testcase)
            run_testcase("\n".join(testcase))
            return

        output = capture_output(run_testcase, "\n".join(testcase))

        print(output)

        cmp_output = compare_output(output, os.path.join(test_folder, input_file.replace("input", "output")))

        if cmp_output:
            print(f"Testcase {input_file} passed")
        else:
            print(f"Testcase {input_file} failed")
            sys.exit(1)

        print()


if __name__ == "__main__":
    if os.getenv("mode") != "dev":
        ic.disable()
    main()
