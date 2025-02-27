def insert_after_index(input_list):
    """
    Insert 43 after index 95 in a list and return the updated list.
    """
    output_list = input_list[:]
    output_list.insert(96, 43)
    return output_list