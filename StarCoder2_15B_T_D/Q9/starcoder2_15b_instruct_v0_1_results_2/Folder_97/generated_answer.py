def all_odd_ints_inclusive(ints):
    """
    Given a list of integers, return all the odd integers from index 40 to index 80, both inclusive.
    If no odd integers exist in the specified range, return an empty list.
    """
    return [x for x in ints[40:81] if x % 2 == 1]