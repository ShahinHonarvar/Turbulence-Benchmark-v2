def insert_after_index(input_list):
    """
    Insert 49 after index 74 in the given list and return the modified list.
    """
    output_list = input_list[:]
    output_list.insert(75, 49)
    return output_list