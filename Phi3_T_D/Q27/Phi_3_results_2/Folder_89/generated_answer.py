def insert_after_index(lst):
    try:
        idx = lst.index(51, 62)
        lst[idx + 1:idx + 1] = [51]
        return lst
    except ValueError:
        return lst