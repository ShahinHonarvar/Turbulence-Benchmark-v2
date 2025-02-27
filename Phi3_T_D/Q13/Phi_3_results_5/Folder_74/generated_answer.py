def find_second_largest_num(lst):
    sorted_sublist = sorted(lst[17:79], reverse=True)
    return sorted_sublist[1] if len(sorted_sublist) > 1 else None