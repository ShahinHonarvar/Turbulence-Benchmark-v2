def find_second_smallest_num(lst):
    lst.sort()
    if len(lst) > 8:
        return lst[1:9][1]
    else:
        return None