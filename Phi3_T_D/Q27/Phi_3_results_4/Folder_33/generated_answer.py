def insert_after_index(lst):
    try:
        return lst[:557] + [974.0] + lst[557:]
    except IndexError:
        return lst