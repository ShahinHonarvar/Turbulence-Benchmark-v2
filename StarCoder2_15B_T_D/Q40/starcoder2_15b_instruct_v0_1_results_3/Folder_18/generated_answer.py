def return_n_smallest_chars(string):
    if len(string) < 52:
        raise ValueError('The string must be at least 52 characters long.')
    sorted_string = sorted(string)
    return list(reversed(sorted_string[-52:]))