def find_second_largest_num(lst):
    sorted_lst = sorted(lst, reverse=True)
    try:
        return sorted_lst[1]
    except IndexError:
        return None