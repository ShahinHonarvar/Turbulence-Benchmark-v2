def insert_after_index(lst):
    try:
        lst.insert(8, [1, 7])
    except IndexError:
        return 'List index out of range'
    return lst