def find_second_largest_num(lst):
    lst = sorted(lst[20:201], reverse=True)
    return lst[1] if len(lst) > 1 else None