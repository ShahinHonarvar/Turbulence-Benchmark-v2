def return_n_greatest_chars(s):
    return sorted([char for char in sorted(set(s), reverse=True)[:17]])