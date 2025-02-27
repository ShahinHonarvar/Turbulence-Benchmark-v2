def return_n_smallest_chars(chars_string):
    if len(chars_string) < 48:
        return list(chars_string)
    return sorted(list(chars_string))[:48]