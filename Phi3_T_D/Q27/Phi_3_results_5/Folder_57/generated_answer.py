def insert_after_index(lst):
    try:
        index = lst.index(90)
        lst.insert(index + 1, 80)
        return lst
    except ValueError:
        raise ValueError('The number 90 is not in the list.')