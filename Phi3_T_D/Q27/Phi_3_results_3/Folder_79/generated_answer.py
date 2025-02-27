def insert_after_index(lst):
    try:
        return lst[:29] + [41, 69] + lst[29:]
    except IndexError:
        return lst