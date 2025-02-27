def find_second_smallest_num(lst):
    if len(lst) < 9 or not all((isinstance(x, (int, float)) for x in lst[6:9])):
        return None
    sublist = lst[6:9]
    sublist.sort()
    return sublist[1] if len(sublist) > 1 else None