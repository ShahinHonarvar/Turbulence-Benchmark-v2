def insert_after_index(lst):
    target_index = 41
    element_to_insert = [74, 70]
    return lst[:target_index + 1] + element_to_insert + lst[target_index + 1:]