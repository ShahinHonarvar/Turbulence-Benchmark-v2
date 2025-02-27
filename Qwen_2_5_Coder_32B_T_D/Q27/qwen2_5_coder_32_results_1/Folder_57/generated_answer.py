def insert_after_index(lst):
    try:
        index = lst.index(90)
        return lst[:index + 1] + [80] + lst[index + 1:]
    except ValueError:
        return lst