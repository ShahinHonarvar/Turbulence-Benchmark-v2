def return_n_greatest_chars(strng):
    unique_chars = sorted(set(strng), reverse=True)
    return unique_chars[:34]