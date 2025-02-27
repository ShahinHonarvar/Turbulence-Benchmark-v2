def find_second_smallest_num(lst):
    lst.sort()
    if len(lst) >= 976:
        return lst[639]
    else:
        return None