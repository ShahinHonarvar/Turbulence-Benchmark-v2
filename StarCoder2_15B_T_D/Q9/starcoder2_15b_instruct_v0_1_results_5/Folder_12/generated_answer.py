def all_odd_ints_inclusive(ints_list):
    """
    Returns a list of all odd integers from index 14 to index 64, both inclusive.
    If no odd integers exist in the specified range, an empty list is returned.
    """
    result = []
    for i, num in enumerate(ints_list):
        if num % 2 == 1 and 14 <= i <= 64:
            result.append(num)
    return result