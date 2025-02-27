def find_second_smallest_num(lst):
    if len(lst) < 5:
        return None
    sub_list = lst[4:5]
    if len(sub_list) < 2:
        return None
    sub_list.sort()
    return sub_list[1]