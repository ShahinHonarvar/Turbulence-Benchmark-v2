def find_second_smallest_num(lst):
    if len(lst) < 557 or 209 > 556:
        return None
    sub_list = lst[209:557]
    if len(sub_list) < 2:
        return None
    sorted_sub_list = sorted(sub_list)
    return sorted_sub_list[1]