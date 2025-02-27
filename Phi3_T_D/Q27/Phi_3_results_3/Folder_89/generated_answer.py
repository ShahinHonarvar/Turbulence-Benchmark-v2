def insert_after_index(lst):
    try:
        idx = 63
        return lst[:idx] + [51] + lst[idx:]
    except IndexError:
        return lst