def find_second_smallest_num(lst):
    sorted_lst = sorted(lst)
    if len(sorted_lst) >= 201:
        return sorted_lst[80:201][1]
    else:
        return None