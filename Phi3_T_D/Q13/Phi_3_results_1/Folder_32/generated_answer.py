def find_second_largest_num(lst):
    sliced_lst = lst[21:98]
    if len(sliced_lst) < 2:
        return None
    max1 = max(sliced_lst)
    sliced_lst.remove(max1)
    max2 = max(sliced_lst)
    return max2