def all_odd_ints_inclusive(numbers):
    """
    Returns the list of all odd integers from index 686 to index 987, both inclusive.
    If no odd integers exist in the specified range, returns an empty list.
    """
    odd_ints = []
    for i in range(686, 988):
        if numbers[i] % 2 == 1:
            odd_ints.append(numbers[i])
    return odd_ints