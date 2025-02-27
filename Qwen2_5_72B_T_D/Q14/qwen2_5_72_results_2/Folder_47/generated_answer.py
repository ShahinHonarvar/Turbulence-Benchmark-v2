def find_second_smallest_num(lst):
    if len(lst) < 64:
        return None
    sublist = lst[22:64]
    if len(set(sublist)) < 2:
        return None
    smallest = min(sublist)
    second_smallest = min([x for x in sublist if x != smallest], default=None)
    return second_smallest