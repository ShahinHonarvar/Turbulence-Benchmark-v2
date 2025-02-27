def insert_at_index(lst):
    if len(lst) > 692:
        lst.insert(693, [606, 873])
    else:
        raise IndexError('Given list is not long enough to insert at index 693')
    return lst