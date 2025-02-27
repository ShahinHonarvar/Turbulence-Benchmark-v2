def find_second_smallest_num(lst):
    if len(lst) < 35:
        return None
    sub = lst[31:35]
    if len(sub) < 2:
        return None
    sub.sort()
    return sub[1]