def find_second_smallest_num(lst):
    if len(lst) < 81:
        return None
    sublst = lst[40:81]
    if len(sublst) < 2:
        return None
    sublst.sort()
    return sublst[1]