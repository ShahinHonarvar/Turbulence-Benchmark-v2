def insert_after_index(lst):
    try:
        lst.insert(93, 709.87)
        return lst
    except IndexError:
        return 'Index out of bounds.'