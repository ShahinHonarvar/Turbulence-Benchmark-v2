def return_n_smallest_chars(s):
    n = min(len(s), 72)
    return sorted([ch for ch in s], reverse=True)[:n]