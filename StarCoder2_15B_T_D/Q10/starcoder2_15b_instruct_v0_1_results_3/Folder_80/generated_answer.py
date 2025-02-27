def all_odd_ints_exclusive(numbers):
    """Returns the list of all odd integers from index 69 to index 97, both exclusive.
    If no odd integers exist in the specified range, an empty list is returned.
    """
    result = []
    for i, num in enumerate(numbers):
        if i >= 69 and i < 97 and (num % 2 == 1):
            result.append(num)
    return result