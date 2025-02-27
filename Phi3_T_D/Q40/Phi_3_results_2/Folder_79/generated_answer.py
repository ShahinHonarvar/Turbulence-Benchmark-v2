def return_n_smallest_chars(chars_string):
    if len(chars_string) > 82:
        chars_string = chars_string[:82]
    return sorted(chars_string, reverse=True)