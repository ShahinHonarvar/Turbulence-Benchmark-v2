def find_second_smallest_num(lst):
    sliced_list = sorted(lst[27:32 + 1])
    if len(sliced_list) > 1:
        return sliced_list[1]
    return None