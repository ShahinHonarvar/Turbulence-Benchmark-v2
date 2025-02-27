def all_odd_ints_exclusive(numbers):
    """
    Given a list of integers, returns the list of all odd integers from index 36 to index 54, both exclusive.
    If no odd integers exist in the specified range, returns an empty list.
    """
    odd_ints = []
    for i, num in enumerate(numbers):
        if i >= 36 and i < 54 and (num % 2 == 1):
            odd_ints.append(num)
    return odd_ints