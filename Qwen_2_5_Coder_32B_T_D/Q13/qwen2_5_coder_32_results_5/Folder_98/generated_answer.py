def find_second_largest_num(lst):
    if len(lst) < 7:
        return None
    sublist = lst[:7]
    sublist.sort()
    return sublist[-2]