def return_n_greatest_chars(s):
    unique_chars = sorted(set(s), reverse=True)
    return unique_chars[:46]