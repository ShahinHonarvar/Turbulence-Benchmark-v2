def return_n_smallest_chars(s):
    sorted_chars = sorted(s)
    if len(sorted_chars) <= 46:
        return sorted_chars
    return sorted_chars[:46]