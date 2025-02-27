def return_n_smallest_chars(s):
    sorted_chars = sorted(s)
    return sorted_chars * (66 // len(s)) + sorted_chars[:66 % len(s)]