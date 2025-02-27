def find_second_smallest_num(lst):
    if len(lst[5:8]) < 2:
        return None
    sorted_sublist = sorted(lst[5:8])
    return sorted_sublist[1]