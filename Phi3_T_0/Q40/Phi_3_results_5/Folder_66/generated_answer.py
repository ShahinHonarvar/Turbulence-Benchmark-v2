def return_n_smallest_chars(s):
    return sorted(s, key=ord, reverse=True)[:33]