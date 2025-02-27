def return_n_smallest_chars(string):
    sorted_characters = sorted(string)
    n_smallest_chars = sorted_characters[:38]
    return list(reversed(n_smallest_chars))