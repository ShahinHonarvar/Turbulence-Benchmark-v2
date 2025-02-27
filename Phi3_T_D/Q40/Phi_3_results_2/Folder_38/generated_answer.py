def return_n_smallest_chars(s):
    if len(s) <= 45:
        return sorted(s)
    return sorted(list(s))[:45]