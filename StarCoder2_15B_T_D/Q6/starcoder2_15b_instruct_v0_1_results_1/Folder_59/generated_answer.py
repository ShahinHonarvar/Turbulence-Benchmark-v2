def all_neg_ints_exclusive(lst):
    """Returns the list of all negative integers from index 0 to index 9, both exclusive.
    If no negative integers exist in the specified range, an empty list is returned."""
    output = []
    for num in lst[:10]:
        if num < 0:
            output.append(num)
    return output