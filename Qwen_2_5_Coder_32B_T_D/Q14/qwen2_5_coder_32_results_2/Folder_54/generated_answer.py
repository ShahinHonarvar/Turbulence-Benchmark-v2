def find_second_smallest_num(lst):
    if len(lst) < 87:
        return None
    sub_list = lst[68:87]
    if len(sub_list) < 2:
        return None
    sub_list.sort()
    return sub_list[1]