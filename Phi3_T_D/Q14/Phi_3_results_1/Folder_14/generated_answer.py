def find_second_smallest_num(lst):
    sliced_lst = lst[8:10]
    try:
        return sorted(sliced_lst)[1]
    except IndexError:
        return None