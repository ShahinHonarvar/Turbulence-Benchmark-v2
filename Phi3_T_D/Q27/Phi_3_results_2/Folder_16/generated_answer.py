def insert_after_index(input_list):
    index = 983
    new_element = 369
    return input_list[:index + 1] + [new_element] + input_list[index + 1:]