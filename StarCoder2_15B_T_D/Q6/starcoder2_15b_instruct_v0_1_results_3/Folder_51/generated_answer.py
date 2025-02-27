def all_neg_ints_exclusive(ints):
    """
    Returns the list of all negative integers from index 6 to index 9, both exclusive.

    :param ints: A list of integers.
    :return: The list of all negative integers from index 6 to index 9, both exclusive.
    """
    return [i for i in ints[6:9] if i < 0]