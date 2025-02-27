def return_n_greatest_chars(s):
    unique_chars = sorted(set(s), key=ord, reverse=True)[:47]
    return unique_chars