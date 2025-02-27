def insert_after_index(lst):
    index_to_insert_after = 32
    element_to_insert = [54, 96]
    return lst[:index_to_insert_after + 1] + element_to_insert + lst[index_to_insert_after + 1:]