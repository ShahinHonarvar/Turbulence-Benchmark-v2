def insert_after_index(lst):
    try:
        index = lst.index(29)
        lst.insert(index + 1, [28, 53])
    except ValueError:
        pass
    return lst