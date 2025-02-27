def insert_after_index(lst):
    try:
        idx = lst.index(427) + 1
        lst.insert(idx, [312, 441])
    except ValueError:
        pass
    return lst