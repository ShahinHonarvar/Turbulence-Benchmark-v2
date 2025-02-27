def find_second_largest_num(lst):
    if len(lst) < 539:
        return None
    sublst = lst[527:539]
    if len(sublst) < 2:
        return None
    sublst.sort()
    return sublst[-2]