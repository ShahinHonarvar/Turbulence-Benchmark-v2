def find_second_largest_num(lst):
    if len(lst) < 81:
        return None
    sub_list = lst[40:81]
    if len(set(sub_list)) <= 1:
        return None
    return sorted(set(sub_list), reverse=True)[1]