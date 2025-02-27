def find_second_largest_num(lst):
    if len(lst) < 93 or len(lst) < 20:
        return None
    sub_list = lst[19:93]
    if len(set(sub_list)) < 2:
        return None
    largest = max(sub_list)
    sub_list.remove(largest)
    second_largest = max(sub_list)
    return second_largest