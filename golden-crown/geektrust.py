import os
import sys
from sys import argv

from icecream import ic

from src.testcase import run_testcase
from src.utils import compare_output, capture_output


def main():
    test_folder = "sample_input"
    test_specified = True

    if len(argv) != 2:
        test_specified = False
        for i in os.listdir(test_folder):
            if i.endswith(".txt") and i.startswith("input"):
                argv.append(os.path.join(test_folder, i))

    for file_path in sorted(argv[1:]):
        input_file = os.path.split(file_path)[1]

        f = open(file_path, 'r')
        testcase = [i.strip() for i in f.readlines() if len(i) > 0]
        f.close()

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
