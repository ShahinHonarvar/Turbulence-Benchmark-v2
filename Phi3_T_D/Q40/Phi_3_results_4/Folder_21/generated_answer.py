def return_n_smallest_chars(text):
    if len(text) < 44:
        return sorted(text, reverse=True)
    return sorted(text * 4, reverse=True)[:44]