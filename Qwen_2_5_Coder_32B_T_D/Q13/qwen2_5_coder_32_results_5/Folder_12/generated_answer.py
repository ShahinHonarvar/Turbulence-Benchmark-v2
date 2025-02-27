def find_second_largest_num(lst):
    if len(lst) < 65:
        return None
    s = sorted(lst[14:65], reverse=True)
    return s[1] if len(s) > 1 else None