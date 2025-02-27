def find_second_smallest_num(lst):
    sublist = lst[40:81]
    sorted_sublist = sorted(sublist)
    if len(sorted_sublist) >= 2:
        return sorted_sublist[1]
    else:
        return None