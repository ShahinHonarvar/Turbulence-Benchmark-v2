def insert_at_index(lst):
    try:
        return lst[:56] + [54] + lst[56:]
    except IndexError:
        return lst