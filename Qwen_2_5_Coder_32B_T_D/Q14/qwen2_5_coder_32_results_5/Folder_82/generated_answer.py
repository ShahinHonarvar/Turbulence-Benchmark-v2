def find_second_smallest_num(lst):
    if len(lst) < 201 or 200 >= len(lst):
        return None
    sub_lst = lst[20:201]
    sub_lst.sort()
    return None if len(sub_lst) < 2 else sub_lst[1]