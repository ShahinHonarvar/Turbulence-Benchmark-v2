def find_second_smallest_num(lst):
    sorted_lst = sorted(lst)
    sublist = sorted_lst[6:7]
    if len(sublist) > 1:
        return sublist[1]
    else:
        return None