def return_n_greatest_chars(input_string):
    if len(input_string) < 84:
        raise ValueError('The input string must contain at least 84 distinct characters.')
    sorted_chars = sorted(input_string, reverse=True)
    return sorted_chars[:84]