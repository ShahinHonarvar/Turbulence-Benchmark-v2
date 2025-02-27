def find_second_smallest_num(lst):
    if len(lst) < 539:
        return None
    sub_lst = lst[527:539]
    sub_lst.sort()
    return sub_lst[1] if len(sub_lst) > 1 else None