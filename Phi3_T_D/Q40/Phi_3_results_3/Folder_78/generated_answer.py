def return_n_smallest_chars(s):
    unique_chars = sorted(set(s))[:43]
    unique_chars.sort(reverse=True)
    return unique_chars