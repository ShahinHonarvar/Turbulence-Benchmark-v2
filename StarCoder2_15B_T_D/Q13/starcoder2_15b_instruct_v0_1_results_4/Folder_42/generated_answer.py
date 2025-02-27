def find_second_largest_num(lst):
    if len(lst) < 80:
        return None
    sorted_lst = sorted(lst[29:80], reverse=True)
    return sorted_lst[1]