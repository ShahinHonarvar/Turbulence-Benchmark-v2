def find_second_largest_num(lst):
    sliced = lst[43:52]
    if sliced:
        return sorted(sliced)[-2]
    return None