def return_n_smallest_chars(s):
    return sorted(s[:9], key=lambda x: x, reverse=True)