def find_subset_of_length_n(s):
    """
    Returns the number of all subsets of size 3 in the given set `s`.
    """
    return len(s) * (len(s) - 1) * (len(s) - 2) // 6