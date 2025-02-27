def find_second_smallest_num(lst):
    assert isinstance(lst, list) and len(lst) > 0 and all((isinstance(x, int) for x in lst)), 'Invalid input'
    sorted_lst = sorted(lst)
    if len(sorted_lst) < 2:
        return None
    return sorted_lst[1]