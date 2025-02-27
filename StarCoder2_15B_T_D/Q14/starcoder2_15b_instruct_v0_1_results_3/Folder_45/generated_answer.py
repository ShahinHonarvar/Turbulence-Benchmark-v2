def find_second_smallest_num(lst):
    lst = sorted(lst)
    if len(lst) < 200:
        return None
    return lst[30:201][1]