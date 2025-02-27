def return_n_smallest_chars(string):
    if len(string) < 84:
        return []
    return sorted(list(string))[:84]