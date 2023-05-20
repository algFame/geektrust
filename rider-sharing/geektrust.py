import os
import src

import sys
from sys import argv

from src import compare_output,capture_output

def main():
    test_folder = "sample_input"


    if len(argv) != 2:
        for i in os.listdir(test_folder):
            if i.endswith(".txt") and i.startswith("input"):
                argv.append(os.path.join(test_folder, i))

    for file_path in sorted(argv[1:]):
        print("testcase-",file_path)
        print()
        input_file = os.path.split(file_path)[1]


        f = open(file_path, 'r')
        testcase = [i.strip() for i in f.readlines() if len(i) > 0]
        f.close()


        output = capture_output(src.run_testcase, "\n".join(testcase))

        print(output)

        cmp_output = compare_output(output, os.path.join(test_folder, input_file.replace("input", "output")))

        if cmp_output:
            print("Testcase passed")
        else:
            print(f"Testcase {input_file} failed")
            print()
            sys.exit(1)

        print()

if __name__ == "__main__":
    if os.getenv("mode") != "dev":
        ic.disable()
    main()
