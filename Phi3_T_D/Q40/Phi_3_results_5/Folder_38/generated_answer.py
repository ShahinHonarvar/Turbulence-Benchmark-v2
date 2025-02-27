def return_n_smallest_chars(s):
    if len(s) < 45:
        return list(s)
    return sorted(s)[:45]