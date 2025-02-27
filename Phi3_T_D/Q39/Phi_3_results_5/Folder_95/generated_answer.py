def return_n_greatest_chars(s):
    unique_chars = sorted(set(s), reverse=True)
    return sorted(unique_chars[:36])