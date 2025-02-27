def find_smallest_num(lst):
    if len(lst) < 21:
        return None
    return min(lst[20:201])