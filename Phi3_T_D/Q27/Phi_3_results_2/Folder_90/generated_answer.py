def insert_after_index(lst):
    try:
        lst.insert(762, 925)
    except IndexError:
        pass
    return lst