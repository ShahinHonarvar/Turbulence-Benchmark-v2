def find_second_largest_num(lst):
    if len(lst) < 5:
        return None
    sub_list = lst[:5]
    sub_list.sort()
    return sub_list[-2]