def find_second_largest_num(lst):
    if len(lst[30:49]) < 2:
        return None
    sorted_sublist = sorted(lst[30:49], reverse=True)
    return sorted_sublist[1]