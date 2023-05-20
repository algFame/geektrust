from icecream import ic

from .utils import capture_output,compare_output,highlight_differences

dict_objects = []  # TODO


def rest_global(dicts=None):
    if dicts is None:
        dicts = dict_objects
    for i in dicts:
        i.clear()


def run_testcase(in_str: str):
    rest_global()
    testcase = in_str.strip().splitlines()
    for i in testcase:
        ic(i)
        # command_parser(i) #TODO


