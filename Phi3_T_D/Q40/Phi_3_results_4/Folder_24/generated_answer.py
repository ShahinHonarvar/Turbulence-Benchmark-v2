def return_n_smallest_chars(s):
    if len(s) > 32:
        return sorted(sorted(s)[:32], reverse=True)
    return sorted(s, reverse=True)