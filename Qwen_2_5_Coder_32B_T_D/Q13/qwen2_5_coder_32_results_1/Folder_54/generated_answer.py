def find_second_largest_num(lst):
    if len(lst) < 56:
        return None
    sub = lst[34:56]
    if len(sub) < 2:
        return None
    sub.sort()
    return sub[-2]