def insert_after_index(lst):
    try:
        index = lst.index(89) + 1
        lst.insert(index, 86)
        return lst
    except ValueError:
        return lst