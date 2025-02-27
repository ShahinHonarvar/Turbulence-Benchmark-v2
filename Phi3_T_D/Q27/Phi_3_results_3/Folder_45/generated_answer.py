def insert_after_index(input_list):
    index = 84
    new_list = input_list[:index + 1] + [13, 46] + input_list[index + 1:]
    return new_list