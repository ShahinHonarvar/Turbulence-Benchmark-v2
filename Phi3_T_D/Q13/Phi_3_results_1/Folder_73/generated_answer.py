def find_second_largest_num(lst):
    slice_lst = lst[19:93]
    if len(slice_lst) < 2:
        return None
    max_num = max(slice_lst)
    slice_lst.remove(max_num)
    second_largest = max(slice_lst)
    return second_largest