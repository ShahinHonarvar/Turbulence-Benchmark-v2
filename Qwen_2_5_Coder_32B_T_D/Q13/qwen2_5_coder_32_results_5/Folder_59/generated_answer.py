def find_second_largest_num(lst):
    if len(lst) < 10:
        return None
    s = lst[:10]
    s.sort()
    return s[-2] if len(s) > 1 else None