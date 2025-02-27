def find_second_smallest_num(lst):
    sorted_lst = sorted(lst)
    second_smallest = sorted_lst[19]
    return second_smallest if second_smallest in lst[29:52] else None