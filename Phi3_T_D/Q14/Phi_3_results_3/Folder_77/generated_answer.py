def find_second_smallest_num(lst):
    sliced_lst = lst[639:976]
    if len(sliced_lst) < 2:
        return None
    sorted_subset = sorted(sliced_lst)
    return sorted_subset[1]