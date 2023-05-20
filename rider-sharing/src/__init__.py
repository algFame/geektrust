from icecream import ic

from .utils import *

from .rider_sharing import command_parser, drivers,matched,riders,rides

dict_objects = [drivers,matched,riders,rides]

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
        command_parser(i)


