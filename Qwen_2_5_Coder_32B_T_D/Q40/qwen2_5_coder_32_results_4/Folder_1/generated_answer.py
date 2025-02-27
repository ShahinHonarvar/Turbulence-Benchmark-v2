def return_n_smallest_chars(s):
    return sorted(sorted(list(s))[:11], reverse=True)