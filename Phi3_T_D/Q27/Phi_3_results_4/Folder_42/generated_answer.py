def insert_after_index(lst):
    index_to_insert = 44
    insert = [40, 27]
    return lst[:index_to_insert + 1] + insert + lst[index_to_insert + 1:]