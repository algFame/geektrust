from icecream import ic

dict_objects = []  # TODO:


def reset_global(dicts=None):
    if dicts is None:
        dicts = dict_objects
    for i in dicts:
        i.clear()


def run_testcase(in_str: str):
    reset_global()
    testcase = in_str.strip().splitlines()
    for i in testcase:
        ic(i)
        # TODO:
