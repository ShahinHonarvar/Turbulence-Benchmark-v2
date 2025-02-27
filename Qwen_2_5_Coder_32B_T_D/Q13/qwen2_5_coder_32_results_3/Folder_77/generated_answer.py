def find_second_largest_num(lst):
    if len(lst) < 539:
        return None
    sub = lst[527:539]
    if len(sub) < 2:
        return None
    sub.sort()
    return sub[-2]