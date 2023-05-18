import os
from sys import argv

from src.rider_sharing import *


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
    if len(argv) != 2:
        argv.append("sample_input/input.txt")

    file_path = argv[-1]
    f = open(file_path, 'r')
    testcase = [i.strip() for i in f.readlines() if len(i) > 0]
    for i in testcase:
        ic(i)
        command_parser(i)
    f.close()


if __name__ == "__main__":
    if os.getenv("mode") != "dev":
        ic.disable()
    main()
