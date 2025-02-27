def insert_after_index(input_list):
    index_to_insert = 42
    value_to_insert = 53
    return input_list[:index_to_insert + 1] + [value_to_insert] + input_list[index_to_insert + 1:]