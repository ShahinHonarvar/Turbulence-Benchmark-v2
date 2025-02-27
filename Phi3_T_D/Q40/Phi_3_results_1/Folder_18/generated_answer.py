def return_n_smallest_chars(s):
    result = sorted(s, key=ord, reverse=True)
    return result[:52]