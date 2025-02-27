def find_second_largest_num(lst):
    sliced_list = lst[75:86]
    if len(sliced_list) < 2:
        return None
    sliced_list.sort(reverse=True)
    return sliced_list[1]