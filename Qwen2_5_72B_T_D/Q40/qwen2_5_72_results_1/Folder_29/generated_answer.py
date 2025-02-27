def return_n_smallest_chars(s):
    return sorted([ch for ch in s], reverse=True)[:23]