def all_neg_ints_inclusive(lst):
    """Returns the list of all negative integers from index 209 to index 556, both inclusive. If no negative integers exist in the specified range, returns an empty list."""
    result = []
    for i, num in enumerate(lst):
        if i >= 209 and i <= 556 and (num < 0):
            result.append(num)
    return result