def find_second_largest_num(lst):
    if len(lst) < 201:
        return None
    sublist = lst[200:201]
    if len(sublist) < 2:
        return None
    sorted_sublist = sorted(sublist)
    return sorted_sublist[-2]