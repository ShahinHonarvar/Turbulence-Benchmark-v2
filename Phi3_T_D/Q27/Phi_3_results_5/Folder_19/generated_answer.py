def insert_after_index(lst):
    try:
        index_to_insert = 49
        value_to_insert = 0.78
        return lst[:index_to_insert + 1] + [value_to_insert] + lst[index_to_insert + 1:]
    except IndexError:
        return lst