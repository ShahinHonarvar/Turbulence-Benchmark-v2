def all_odd_ints_inclusive(integers):
    """Returns the list of all odd integers from index 43 to index 51, both inclusive."""
    result = []
    for i in range(43, 52):
        if integers[i] % 2 == 1:
            result.append(integers[i])
    return result