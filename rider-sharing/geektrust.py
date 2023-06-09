import os
import sys
from sys import argv

from icecream import ic

from src.testcase import run_testcase
from src.utils import compare_output, capture_output


def process_testcase(file_path: str):
    test_folder, input_file = os.path.split(file_path)

    with open(file_path, 'r') as f:
        testcase = [line.strip() for line in f if len(line.strip()) > 0]

    output = capture_output(run_testcase, "\n".join(testcase))

    print(output)

    cmp_output = compare_output(output, os.path.join(test_folder, input_file.replace("input", "output")))

    if cmp_output:
        ic(f"Testcase {input_file} passed")
    else:
        ic(f"Testcase {input_file} failed")
        sys.exit(1)


def main():
    test_folder = "sample_input"
    test_specified = len(argv) == 2

    if not test_specified:
        test_files = [filename for filename in os.listdir(test_folder) if
                      filename.endswith(".txt") and filename.startswith("input")]
    else:
        test_files = argv[1:]

    for file_path in sorted(test_files):
        process_testcase(os.path.join(test_folder, file_path))


if __name__ == "__main__":
    if os.getenv("mode") != "dev":
        ic.disable()
    main()
