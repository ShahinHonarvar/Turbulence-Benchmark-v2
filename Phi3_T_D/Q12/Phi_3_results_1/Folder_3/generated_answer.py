def find_smallest_num(lst):
    if len(lst) < 31:
        return None
    return min(lst[20:31])