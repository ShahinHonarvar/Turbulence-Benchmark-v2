def all_odd_ints_inclusive(numbers):
    """Returns the list of all odd integers from index 42 to index 68, both inclusive.
    If no odd integers exist in the specified range, returns an empty list.
    """
    odd_ints = []
    for i, num in enumerate(numbers):
        if i >= 42 and i <= 68 and (num % 2 == 1):
            odd_ints.append(num)
    return odd_ints