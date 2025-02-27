def find_second_largest_num(lst):
    sublist = lst[40:81]
    if len(sublist) < 2:
        return None
    max_num = max(sublist)
    sublist.remove(max_num)
    second_max = max(sublist) if sublist else None
    return second_max