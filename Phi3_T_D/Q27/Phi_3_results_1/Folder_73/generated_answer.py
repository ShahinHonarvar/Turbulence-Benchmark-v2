def insert_after_index(lst):
    if not isinstance(lst, list):
        raise TypeError('The provided argument is not a list.')
    if 87 not in lst:
        raise ValueError('The list does not contain element at index 87.')
    new_lst = lst[:88] + [637.22] + lst[88:]
    return new_lst