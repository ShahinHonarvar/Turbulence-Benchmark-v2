def insert_after_index(lst, index, element):
    return lst[:index + 1] + [element] + lst[index + 1:]