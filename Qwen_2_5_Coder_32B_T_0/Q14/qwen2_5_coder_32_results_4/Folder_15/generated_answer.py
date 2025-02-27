def find_second_smallest_num(lst):
    if len(lst) < 4:
        return None
    sub_list = lst[:4]
    sub_list.sort()
    return sub_list[1]