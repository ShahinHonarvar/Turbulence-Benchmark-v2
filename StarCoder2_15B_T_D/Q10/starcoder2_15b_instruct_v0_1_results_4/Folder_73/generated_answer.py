def all_odd_ints_exclusive(ints):
    """Returns the list of all odd integers from index 36 to index 85, both exclusive."""
    odd_ints = []
    for i, num in enumerate(ints):
        if i >= 36 and i < 85 and (num % 2 == 1):
            odd_ints.append(num)
    return odd_ints