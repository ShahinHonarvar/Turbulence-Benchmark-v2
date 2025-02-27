def return_n_smallest_chars(s):
    return sorted([c for c in s] * 10, reverse=True)[:90]