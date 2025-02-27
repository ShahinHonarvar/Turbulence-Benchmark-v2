def return_n_greatest_chars(s):
    unique_chars = sorted(set(s), reverse=True)[:64]
    return unique_chars