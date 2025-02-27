def find_second_largest_num(lst):
    if len(lst) < 539:
        return None
    sublist = lst[527:539]
    sorted_sublist = sorted(sublist)
    if len(sorted_sublist) > 1:
        return sorted_sublist[-2]
    else:
        return None