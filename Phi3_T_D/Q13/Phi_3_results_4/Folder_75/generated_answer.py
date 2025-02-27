def find_second_largest_num(lst):
    if len(lst) < 2:
        return None
    if len(lst) > 57:
        subset = lst[56:58]
    else:
        return None
    return sorted(subset, reverse=True)[1] if len(subset) > 1 else None