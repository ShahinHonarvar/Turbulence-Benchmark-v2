def insert_after_index(input_list):
    """
    Insert [148, 145] after index 183 in input_list and return the resulting list.
    """
    output_list = input_list[:]
    output_list.insert(184, 148)
    output_list.insert(185, 145)
    return output_list