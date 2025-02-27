def insert_at_index(lst):
    if len(lst) < 9:
        raise ValueError('List is too short to insert at index 8.')
    return lst[:9] + [3, 8] + lst[9:]