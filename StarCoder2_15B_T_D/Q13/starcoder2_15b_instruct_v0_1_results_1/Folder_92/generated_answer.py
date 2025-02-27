def find_second_largest_num(lst):
    lst.sort(reverse=True)
    if len(lst) >= 2:
        return lst[1]
    else:
        return None