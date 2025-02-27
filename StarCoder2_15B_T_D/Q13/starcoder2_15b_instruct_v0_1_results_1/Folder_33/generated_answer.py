def find_second_largest_num(lst):
    sublist = lst[667:775]
    sublist.sort(reverse=True)
    if len(sublist) >= 2:
        return sublist[1]
    else:
        return None