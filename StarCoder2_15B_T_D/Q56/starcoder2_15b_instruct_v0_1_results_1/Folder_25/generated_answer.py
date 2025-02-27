import itertools

def all_substring_of_size_n(s):
    """
    Returns a list of all distinct substrings of length n with no duplicate characters in the given string.
    """
    n = 67
    substrings = [''.join(c) for c in itertools.combinations(s, n)]
    unique_substrings = []
    for substring in substrings:
        if len(set(substring)) == n:
            unique_substrings.append(substring)
    return unique_substrings