def insert_after_index(lst):
    try:
        lst.insert(48 + 1, [86, 77])
        return lst
    except IndexError:
        print('Index out of range')