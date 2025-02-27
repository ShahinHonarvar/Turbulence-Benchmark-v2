from itertools import islice

def all_odd_ints_exclusive(int_list):
    return list(filter(lambda x: x % 2 != 0, islice(int_list, 36, 54)))