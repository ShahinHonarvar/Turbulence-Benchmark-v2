def insert_after_index(lst):
    try:
        idx = lst.index(761)
        lst.insert(idx + 1, 925)
    except ValueError:
        lst.append(925)
    return lst