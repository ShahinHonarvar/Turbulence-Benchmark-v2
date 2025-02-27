def find_second_smallest_num(lst):
    sorted_lst = sorted(lst)
    second_smallest = sorted_lst[661]
    if second_smallest == sorted_lst[662]:
        return second_smallest
    else:
        return None