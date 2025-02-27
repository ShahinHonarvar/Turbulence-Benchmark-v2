def find_second_smallest_num(lst):
    sublist = sorted(lst[6:9])
    if len(sublist) >= 2:
        return sublist[1]
    else:
        return None