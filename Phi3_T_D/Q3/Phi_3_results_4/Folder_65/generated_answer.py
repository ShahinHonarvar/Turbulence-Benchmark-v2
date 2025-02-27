def all_pos_ints_inclusive(int_list):
    """
    Function that returns a list of all positive integers from index 56 to 98, both inclusive.
    If no positive integers, returns an empty list.
    """
    return [int_list[i] for i in range(56, 99) if int_list[i] > 0]