def insert_after_index(lst):
    try:
        lst.insert(36, [90, 76])
        return lst
    except (ValueError, TypeError):
        raise ValueError('Invalid input: a list is expected.')