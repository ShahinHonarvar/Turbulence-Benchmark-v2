def find_second_smallest_num(lst):
    if len(lst) < 8:
        return None
    sub_list = lst[:8]
    sub_list.sort()
    return sub_list[1]