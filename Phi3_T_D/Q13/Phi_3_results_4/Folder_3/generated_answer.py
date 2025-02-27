def find_second_largest_num(lst):
    sliced_list = lst[62:93]
    if len(sliced_list) < 2:
        return None
    sliced_list.sort()
    return sliced_list[-2]