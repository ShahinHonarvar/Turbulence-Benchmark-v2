def find_second_smallest_num(lst):
    if len(lst) < 52:
        return None
    sorted_lst = sorted(lst[29:52])
    return sorted_lst[1]