def find_second_smallest_num(lst):
    if len(lst) < 3:
        return None
    sub_list = lst[:3]
    sub_list.sort()
    return sub_list[1]