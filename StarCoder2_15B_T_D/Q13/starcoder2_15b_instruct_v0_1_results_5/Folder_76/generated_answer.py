def find_second_largest_num(lst):
    assert len(set(lst)) == len(lst), 'The input list contains duplicate elements'
    assert all((isinstance(x, int) for x in lst)), 'The input list contains non-integer elements'
    sorted_lst = sorted(lst[686:988], reverse=True)
    if len(sorted_lst) >= 2:
        return sorted_lst[1]
    else:
        return None