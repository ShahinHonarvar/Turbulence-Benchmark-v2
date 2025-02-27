def return_n_greatest_chars(s):
    sorted_chars = sorted(s)
    if len(sorted_chars) > 19:
        return sorted_chars[-19:]
    return sorted_chars